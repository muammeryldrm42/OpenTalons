import { describe,it,expect } from 'vitest'; import { redact } from './index'; describe('utils',()=>it('redacts',()=>expect(redact('sk-ABCDEFGH12345678')).toContain('REDACTED')));
