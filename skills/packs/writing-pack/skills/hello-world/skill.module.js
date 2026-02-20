import manifest from './manifest.json' assert { type: 'json' };
export default { manifest, async run(input, ctx){ return { ok:true, echo: input, runId: ctx.runId }; } };
