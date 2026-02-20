import { describe,it,expect } from 'vitest'; import { getManifest } from './index'; describe('ext',()=>it('ok',()=>expect(getManifest().name).toBeTruthy()));
