export type PolicyProfile = "solo" | "team" | "marketplace";
export type Permission = "net:read" | "fs:read" | "fs:write" | "secrets:read";
export interface SkillManifest { name: string; version: string; description?: string; category?: string; tags?: string[]; permissions: Permission[]; limits?: { timeoutMs?: number; maxToolOutputBytes?: number; maxModelOutputBytes?: number; }; policyHints?: { netAllowlist?: string[]; notes?: string; }; compatibility?: { coreRange?: string; }; }
export interface SkillContext { runId: string; profile: PolicyProfile; meta?: Record<string, unknown>; }
export interface ToolCall<TArgs=unknown> { tool: string; args: TArgs; }
export interface ToolResult<TResult=unknown> { ok: boolean; result?: TResult; error?: { message: string; code?: string }; }
export interface ToolInvoker { call<TArgs,TResult>(call: ToolCall<TArgs>): Promise<ToolResult<TResult>>; }
export interface SkillModule<TInput=unknown,TOutput=unknown> { manifest: SkillManifest; run(input: TInput, ctx: SkillContext, tools: ToolInvoker): Promise<TOutput>; }
export type TraceEvent =
  | { type: "run_start"; runId: string; at: string; profile: PolicyProfile; skill: string }
  | { type: "tool_call"; runId: string; at: string; tool: string }
  | { type: "tool_result"; runId: string; at: string; tool: string; ok: boolean }
  | { type: "run_end"; runId: string; at: string; ok: boolean };
