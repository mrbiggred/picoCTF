
void FUN_0044afed(void)

{
  code *UNRECOVERED_JUMPTABLE;
  uint *puVar1;
  undefined4 uVar2;
  code *unaff_RBP;
  long unaff_retaddr;
  undefined8 local_38;
  long lStack_30;
  ulong uStack_28;
  code *pcStack_20;
  long lStack_18;
  undefined8 local_10;
  undefined8 local_8;
  
  syscall();
  puVar1 = (uint *)(unaff_retaddr + 0x13);
  lStack_18 = (long)(unaff_RBP + -0xb) - (ulong)*(uint *)(unaff_RBP + -0xb);
  local_10 = 2;
  syscall();
  local_8 = 9;
  syscall();
  pcStack_20 = unaff_RBP + (9 - lStack_18);
  uStack_28 = (ulong)pcStack_20 & 0xfffffffffffff000;
  lStack_30 = (long)puVar1 + ((((ulong)*puVar1 - lStack_18) + 9) - uStack_28);
  uVar2 = (undefined4)(uStack_28 >> 0x20);
  local_38 = CONCAT44(uVar2,*puVar1);
  UNRECOVERED_JUMPTABLE = (code *)((long)puVar1 + (9 - lStack_18));
  (*unaff_RBP)(unaff_retaddr + 0x1f,CONCAT44(uVar2,*(undefined4 *)(unaff_retaddr + 0x17)),
               UNRECOVERED_JUMPTABLE,&local_38,*(undefined4 *)(unaff_retaddr + 0x1b),0);
  pcStack_20 = (code *)0xa;
  syscall();
                    /* WARNING: Could not recover jumptable at 0x0044b0a4. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (*UNRECOVERED_JUMPTABLE)(uStack_28,lStack_30,5,local_38);
  return;
}

