import type { SkillModule, SkillContext, ToolInvoker, ToolCall, ToolResult } from "@opentalons/contracts";
import type { PolicyConfig } from "./policy.js";
import { PolicyEngine } from "./policy.js";
import { isoNow } from "@opentalons/utils";

export class Runner {
  async run<TIn,TOut>(skill: SkillModule<TIn,TOut>, input:TIn, opts:{ profile: SkillContext["profile"]; policy: Omit<PolicyConfig,"profile"> }) : Promise<TOut> {
    const ctx: SkillContext = { runId: crypto.randomUUID(), profile: opts.profile };
    const policy = new PolicyEngine({ profile: opts.profile, ...opts.policy });
    const tools: ToolInvoker = {
      call: async <A,R>(call: ToolCall<A>): Promise<ToolResult<R>> => {
        const d = policy.decide(call as any, skill.manifest.permissions);
        if (!d.allow) return { ok:false, error:{ message:d.reason??"Blocked", code:"POLICY_BLOCK" } };
        return { ok:false, error:{ message:`${call.tool} not implemented`, code:"NOT_IMPL" } };
      }
    };
    return skill.run(input, ctx, tools);
  }
}
