export const isoNow=()=>new Date().toISOString();
export const redact=(t:string)=>t.replace(/(sk-[A-Za-z0-9]{8,})/g,'sk-REDACTED');
