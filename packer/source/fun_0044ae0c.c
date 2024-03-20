
void FUN_0044ae0c(undefined4 *param_1,undefined8 param_2,undefined8 param_3,uint param_4)

{
  undefined4 uVar1;
  uint uVar2;
  undefined4 *puVar3;
  undefined uVar4;
  ulong unaff_RBP;
  
  puVar3 = (undefined4 *)((long)param_1 + unaff_RBP);
  uVar4 = *(undefined *)puVar3;
  if ((5 < param_4) && (unaff_RBP < 0xfffffffffffffffd)) {
    uVar2 = param_4 - 4;
    do {
      param_4 = uVar2;
      uVar1 = *puVar3;
      puVar3 = puVar3 + 1;
      *param_1 = uVar1;
      param_1 = param_1 + 1;
      uVar2 = param_4 - 4;
    } while (3 < param_4);
    uVar4 = *(undefined *)puVar3;
    if (param_4 == 0) {
      return;
    }
  }
  do {
    puVar3 = (undefined4 *)((long)puVar3 + 1);
    *(undefined *)param_1 = uVar4;
    param_4 = param_4 - 1;
    uVar4 = *(undefined *)puVar3;
    param_1 = (undefined4 *)((long)param_1 + 1);
  } while (param_4 != 0);
  return;
}

