import { spawn } from 'child_process';
import fs from 'fs';
import path from 'path';
import { streamText } from 'ai';
import { getStoryModel } from '$lib/api/ai';
import type { StoryModel } from '$lib/config/story';

const decoderPrompt = fs.readFileSync(path.resolve('prompts/prompt_npc.txt'), 'utf-8');

export async function generateDNA(): Promise<string> {
  return new Promise((resolve, reject) => {
    const py = spawn('python', ['scripts/npc_generator.py']);
    let result = '';
    py.stdout.on('data', (d) => (result += d));
    py.stderr.on('data', (err) => reject(err.toString()));
    py.on('close', () => resolve(result.trim()));
  });
}

export function buildPromptFromDNA(dna: string): string {
  return decoderPrompt.replace('**DNA (Internal Reference Only):**', `**DNA (Internal Reference Only):**\n\`${dna}\``);
}

export async function generateNPCFromDNA(model: StoryModel) {
  const dna = await generateDNA();
  const prompt = buildPromptFromDNA(dna);
  const result = await streamText({
    model: getStoryModel(model),
    messages: [{ role: 'user', content: prompt }],
    temperature: 1
  });
  return { stream: result.toAIStream(), dna };
}
