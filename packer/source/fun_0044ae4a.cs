
long FUN_0044ae4a(byte *param_1,uint *param_2,undefined8 param_3,undefined8 param_4,char param_5,
                 undefined8 param_6,long param_7,int param_8,int *param_9)

{
  int iVar1;
  uint uVar2;
  uint uVar3;
  uint extraout_EDX;
  uint unaff_EBX;
  byte bVar4;
  bool bVar5;
  byte bVar6;
  bool bVar7;
  code *unaff_retaddr;
  
  if (param_5 == '\b') {
    do {
      while( true ) {
        bVar6 = *(byte *)param_2;
        bVar4 = CARRY4(unaff_EBX,unaff_EBX);
        unaff_EBX = unaff_EBX * 2;
        if (unaff_EBX == 0) {
          uVar3 = *param_2;
          bVar5 = param_2 < (uint *)0xfffffffffffffffc;
          param_2 = param_2 + 1;
          bVar4 = CARRY4(uVar3,uVar3) || CARRY4(uVar3 * 2,(uint)bVar5);
          unaff_EBX = uVar3 * 2 + (uint)bVar5;
          bVar6 = *(byte *)param_2;
        }
        if (!(bool)bVar4) break;
        param_2 = (uint *)((long)param_2 + 1);
        *param_1 = bVar6;
        param_1 = param_1 + 1;
      }
      while( true ) {
        iVar1 = (*unaff_retaddr)();
        uVar2 = iVar1 * 2 + (uint)bVar4;
        bVar6 = CARRY4(unaff_EBX,unaff_EBX);
        unaff_EBX = unaff_EBX * 2;
        uVar3 = extraout_EDX;
        if (unaff_EBX == 0) {
          uVar3 = *param_2;
          bVar5 = param_2 < (uint *)0xfffffffffffffffc;
          param_2 = param_2 + 1;
          bVar6 = CARRY4(uVar3,uVar3) || CARRY4(uVar3 * 2,(uint)bVar5);
          unaff_EBX = uVar3 * 2 + (uint)bVar5;
          uVar3 = (uint)*(byte *)param_2;
        }
        if ((bool)bVar6) break;
        uVar3 = (*unaff_retaddr)();
        bVar4 = CARRY4(uVar3,uVar3) || CARRY4(uVar3 * 2,(uint)bVar6);
      }
      if (uVar2 < 3) {
        bVar5 = CARRY4(unaff_EBX,unaff_EBX);
        unaff_EBX = unaff_EBX * 2;
        if (unaff_EBX == 0) {
          uVar3 = *param_2;
          bVar7 = param_2 < (uint *)0xfffffffffffffffc;
          param_2 = param_2 + 1;
          bVar5 = CARRY4(uVar3,uVar3) || CARRY4(uVar3 * 2,(uint)bVar7);
          unaff_EBX = uVar3 * 2 + (uint)bVar7;
        }
        if (!bVar5) goto LAB_0044aec3;
LAB_0044aeeb:
        (*unaff_retaddr)();
      }
      else {
        param_2 = (uint *)((long)param_2 + 1);
        uVar3 = ((uVar2 - 3) * 0x100 | uVar3 & 0xff) ^ 0xffffffff;
        if (uVar3 == 0) break;
        if ((uVar3 & 1) != 0) goto LAB_0044aeeb;
LAB_0044aec3:
        bVar5 = CARRY4(unaff_EBX,unaff_EBX);
        unaff_EBX = unaff_EBX * 2;
        if (unaff_EBX == 0) {
          uVar3 = *param_2;
          bVar7 = param_2 < (uint *)0xfffffffffffffffc;
          param_2 = param_2 + 1;
          bVar5 = CARRY4(uVar3,uVar3) || CARRY4(uVar3 * 2,(uint)bVar7);
          unaff_EBX = uVar3 * 2 + (uint)bVar7;
        }
        if (bVar5) goto LAB_0044aeeb;
        do {
          (*unaff_retaddr)();
          bVar5 = CARRY4(unaff_EBX,unaff_EBX);
          unaff_EBX = unaff_EBX * 2;
          if (unaff_EBX == 0) {
            uVar3 = *param_2;
            bVar7 = param_2 < (uint *)0xfffffffffffffffc;
            param_2 = param_2 + 1;
            bVar5 = CARRY4(uVar3,uVar3) || CARRY4(uVar3 * 2,(uint)bVar7);
            unaff_EBX = uVar3 * 2 + (uint)bVar7;
          }
        } while (!bVar5);
      }
      FUN_0044ae0c();
    } while( true );
  }
  *param_9 = (int)param_1 - param_8;
  return (long)param_2 - param_7;
}

