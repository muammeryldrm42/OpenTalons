import type { Permission, PolicyProfile, ToolCall } from "@opentalons/contracts";
export interface PolicyConfig { profile: PolicyProfile; netAllowlist?: string[]; limits: { timeoutMs: number; maxToolOutputBytes: number }; disabledTools?: string[]; }
export class PolicyEngine {
  constructor(private readonly cfg: PolicyConfig) {}
  decide(call: ToolCall, perms: Permission[]) {
    if (this.cfg.disabledTools?.includes(call.tool)) return { allow:false, reason:`Tool disabled: ${call.tool}` };
    const req = call.tool.startsWith("net.") ? "net:read" : call.tool.startsWith("fs.read") ? "fs:read" : call.tool.startsWith("fs.write") ? "fs:write" : call.tool.startsWith("secrets.") ? "secrets:read" : null;
    if (req && !perms.includes(req as any)) return { allow:false, reason:`Missing permission: ${req}` };
    if (call.tool==="net.fetch" && this.cfg.profile==="marketplace") {
      const url=(call.args as any)?.url as string|undefined;
      if (!url) return { allow:false, reason:"Missing url" };
      if (!this.allowed(url)) return { allow:false, reason:"URL not allowed" };
    }
    return { allow:true };
  }
  private allowed(url:string){ const a=this.cfg.netAllowlist??[]; if(!a.length) return false; try{ const u=new URL(url); return a.some(d=>u.hostname===d||u.hostname.endsWith(`.${d}`)); }catch{ return false; } }
}
