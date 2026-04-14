//BORRACRE JOB (ACCT),'FACUNDO',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1)
//STEP1    EXEC PGM=IEFBR14
//DD1      DD  DSN=FACUNDO.TEST.FILE,
//             DISP=(MOD,DELETE,DELETE),
//             SPACE=(TRK,(1,1)),
//             UNIT=SYSDA

//STEP2    EXEC PGM=IEFBR14
//DD1      DD  DSN=FACUNDO.TEST.FILE,
//             DISP=(NEW,CATLG,DELETE),
//             DCB=(RECFM=FB,LRECL=80,BLKSIZE=800),
//             SPACE=(TRK,(2,2)),
//             UNIT=SYSDA

//STEP3    EXEC PGM=IEBGENER
//SYSUT1   DD  *
Este es un ejemplo de uso del archivo
Generado por el JCL
/*
//SYSUT2   DD  DSN=FACUNDO.TEST.FILE,
//             DISP=SHR
//SYSPRINT DD  SYSOUT=*
//SYSIN    DD  DUMMY
