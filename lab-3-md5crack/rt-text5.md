# RTCrack, MD5 on 5

## Table generation

rainbowcrack-1.7-win64>rtgen.exe md5 loweralpha-numeric 5 5 0 3800 600000 0
rainbow table md5_loweralpha-numeric#5-5_0_3800x600000_0.rt parameters
hash algorithm:         md5
hash length:            16
charset name:           loweralpha-numeric
charset data:           abcdefghijklmnopqrstuvwxyz0123456789
charset data in hex:    61 62 63 64 65 66 67 68 69 6a 6b 6c 6d 6e 6f 70 71 72 73 74 75 76 77 78 79 7a 30 31 32 33 34 35 36 37 38 39
charset length:         36
plaintext length range: 5 - 5
reduce offset:          0x00000000
plaintext total:        60466176

sequential starting point begin from 0 (0x0000000000000000)
generating...
262144 of 600000 rainbow chains generated (0 m 26.6 s)
524288 of 600000 rainbow chains generated (0 m 28.0 s)
600000 of 600000 rainbow chains generated (0 m 8.5 s)

## Cracking

```
rainbowcrack-1.7-win64>rcrack.exe ./ -l hash5.txt
1 rainbow tables found
memory available: 1032250982 bytes
memory for rainbow chain traverse: 60800 bytes per hash, 912000 bytes for 15 hashes
memory for rainbow table buffer: 2 x 9600016 bytes
disk: ./\md5_loweralpha-numeric#5-5_0_3800x600000_0.rt: 9600000 bytes read
disk: finished reading all files
plaintext of a92b66a9802704ca8616c4b092378272 is opmen
plaintext of 81466b6bb4be5a48e2230be1338bcde6 is lou0g
plaintext of 836626589007d7dd5304c8d22815fffc is di5gv
plaintext of 1b31905c59f481958d2eb72158c27ac7 is egunb
plaintext of 1b4baba3ae3be69857b323cf6b7fcd80 is sso55
plaintext of 78c1b8edd1bc3ffc438432479289a9e1 is nized
plaintext of 0d5b558d5f6744deaaf5b016c6c77a57 is tpoin
plaintext of a8218c67a5b4e652e30a59372e07df59 is hed4e
plaintext of a74edf83748e3c4fa5f31ec10bad79db is dsmto
plaintext of ddaafa5d551a582bc924d09cc8d33ee5 is aseas
plaintext of 6e313b70d12de950443527a33d802b76 is mlhdi
plaintext of d4efdba5e9725e77c9b9051fa8136f0a is tthel
plaintext of 644674d142ba2174a80889f833b32563 is owso9
plaintext of de952f5454fb0ee79bca249f80e9fe8f is ofror
plaintext of 96f6065d8f2dd1376eff88fba65d1d83 is cance

statistics
----------------------------------------------------------------
plaintext found:                             15 of 15
total time:                                  4.94 s
time of chain traverse:                      3.23 s
time of alarm check:                         1.53 s
time of disk read:                           0.00 s
hash & reduce calculation of chain traverse: 108243000
hash & reduce calculation of alarm check:    41923193
number of alarm:                             144643
performance of chain traverse:               33.46 million/s
performance of alarm check:                  27.37 million/s

result
----------------------------------------------------------------
a92b66a9802704ca8616c4b092378272  opmen  hex:6f706d656e
d4efdba5e9725e77c9b9051fa8136f0a  tthel  hex:747468656c
96f6065d8f2dd1376eff88fba65d1d83  cance  hex:63616e6365
78c1b8edd1bc3ffc438432479289a9e1  nized  hex:6e697a6564
0d5b558d5f6744deaaf5b016c6c77a57  tpoin  hex:74706f696e
ddaafa5d551a582bc924d09cc8d33ee5  aseas  hex:6173656173
a74edf83748e3c4fa5f31ec10bad79db  dsmto  hex:64736d746f
1b31905c59f481958d2eb72158c27ac7  egunb  hex:6567756e62
6e313b70d12de950443527a33d802b76  mlhdi  hex:6d6c686469
de952f5454fb0ee79bca249f80e9fe8f  ofror  hex:6f66726f72
a8218c67a5b4e652e30a59372e07df59  hed4e  hex:6865643465
836626589007d7dd5304c8d22815fffc  di5gv  hex:6469356776
644674d142ba2174a80889f833b32563  owso9  hex:6f77736f39
1b4baba3ae3be69857b323cf6b7fcd80  sso55  hex:73736f3535
81466b6bb4be5a48e2230be1338bcde6  lou0g  hex:6c6f753067
```

# RTcrack, MD5 on 6:

## Table Generation

rainbowcrack-1.7-win64>rtgen.exe md5 loweralpha-numeric 6 6 0 3800 600000 0
rainbow table md5_loweralpha-numeric#6-6_0_3800x600000_0.rt parameters
hash algorithm:         md5
hash length:            16
charset name:           loweralpha-numeric
charset data:           abcdefghijklmnopqrstuvwxyz0123456789
charset data in hex:    61 62 63 64 65 66 67 68 69 6a 6b 6c 6d 6e 6f 70 71 72 73 74 75 76 77 78 79 7a 30 31 32 33 34 35 36 37 38 39
charset length:         36
plaintext length range: 6 - 6
reduce offset:          0x00000000
plaintext total:        2176782336

sequential starting point begin from 0 (0x0000000000000000)
generating...
262144 of 600000 rainbow chains generated (0 m 29.2 s)
524288 of 600000 rainbow chains generated (0 m 31.5 s)
600000 of 600000 rainbow chains generated (0 m 8.5 s)

## Cracking

```
rainbowcrack-1.7-win64>rcrack.exe ./ -l salted6.txt
1 rainbow tables found
memory available: 1022941593 bytes
memory for rainbow chain traverse: 60800 bytes per hash, 912000 bytes for 15 hashes
memory for rainbow table buffer: 2 x 9600016 bytes
disk: ./\md5_loweralpha-numeric#6-6_0_3800x600000_0.rt: 9600000 bytes read
disk: finished reading all files
plaintext of bcd8d08cfe9c57ecc5b9fd4b45d8be77 is egunba
plaintext of 39c7bc504190c8b7c4eedb146cbe7f95 is di5gva
plaintext of 855265960fecd55c76d5928c84b14886 is ofrora
plaintext of 7cc7fdaf74697df714b383e34071b618 is dsmtoa
plaintext of 21a47c906dbbe36e252921753864403e is sso55a
plaintext of 66e76fb30a7e59f1c9e4f748bbb09396 is tthela
plaintext of a9a2500b1222f6f0f16bf52455dfee7c is lou0ga
plaintext of b6b92809cafdb66e092476a53a085aa8 is opmena

statistics
----------------------------------------------------------------
plaintext found:                             8 of 15
total time:                                  4.33 s
time of chain traverse:                      3.38 s
time of alarm check:                         0.92 s
time of disk read:                           0.02 s
hash & reduce calculation of chain traverse: 108243000
hash & reduce calculation of alarm check:    26935429
number of alarm:                             24032
performance of chain traverse:               32.06 million/s
performance of alarm check:                  29.18 million/s

result
----------------------------------------------------------------
66e76fb30a7e59f1c9e4f748bbb09396  tthela  hex:747468656c61
1a10b176c926d5d6ea456117ac754533  <not found>  hex:<not found>
21a47c906dbbe36e252921753864403e  sso55a  hex:73736f353561
7f80e6d582cb2a18a2fe0b83d3afe830  <not found>  hex:<not found>
b6b92809cafdb66e092476a53a085aa8  opmena  hex:6f706d656e61
855265960fecd55c76d5928c84b14886  ofrora  hex:6f66726f7261
189c2f65dfca3a7d44dbf967563a2051  <not found>  hex:<not found>
b8f9c9311827bf24de109c4ed5447b0b  <not found>  hex:<not found>
a9a2500b1222f6f0f16bf52455dfee7c  lou0ga  hex:6c6f75306761
b95fdd0f9f4fe555a4e7b19d18117d60  <not found>  hex:<not found>
bcd8d08cfe9c57ecc5b9fd4b45d8be77  egunba  hex:6567756e6261
7cc7fdaf74697df714b383e34071b618  dsmtoa  hex:64736d746f61
39c7bc504190c8b7c4eedb146cbe7f95  di5gva  hex:646935677661
dee536e9130e8cc2550fed9e9b03a5a3  <not found>  hex:<not found>
7730e6289fc772646d5984c96c446e8f  <not found>  hex:<not found>
```

## Generation: 120,000 entries

```
rainbowcrack-1.7-win64>rtgen.exe md5 loweralpha-numeric 6 6 0 3800 1200000 0
rainbow table md5_loweralpha-numeric#6-6_0_3800x1200000_0.rt parameters
hash algorithm:         md5
hash length:            16
charset name:           loweralpha-numeric
charset data:           abcdefghijklmnopqrstuvwxyz0123456789
charset data in hex:    61 62 63 64 65 66 67 68 69 6a 6b 6c 6d 6e 6f 70 71 72 73 74 75 76 77 78 79 7a 30 31 32 33 34 35 36 37 38 39
charset length:         36
plaintext length range: 6 - 6
reduce offset:          0x00000000
plaintext total:        2176782336

sequential starting point begin from 0 (0x0000000000000000)
generating...
262144 of 1200000 rainbow chains generated (0 m 30.5 s)
524288 of 1200000 rainbow chains generated (0 m 31.7 s)
786432 of 1200000 rainbow chains generated (0 m 31.3 s)
1048576 of 1200000 rainbow chains generated (0 m 32.1 s)
1200000 of 1200000 rainbow chains generated (0 m 18.9 s)
```

## Cracking

```
rainbowcrack-1.7-win64>rcrack.exe ./ -l salted6.txt
1 rainbow tables found
memory available: 1049326387 bytes
memory for rainbow chain traverse: 60800 bytes per hash, 912000 bytes for 15 hashes
memory for rainbow table buffer: 2 x 19200016 bytes
disk: ./\md5_loweralpha-numeric#6-6_0_3800x1200000_0.rt: 19200000 bytes read
disk: finished reading all files
plaintext of 1a10b176c926d5d6ea456117ac754533 is tpoina
plaintext of bcd8d08cfe9c57ecc5b9fd4b45d8be77 is egunba
plaintext of b8f9c9311827bf24de109c4ed5447b0b is mlhdia
plaintext of 7cc7fdaf74697df714b383e34071b618 is dsmtoa
plaintext of 39c7bc504190c8b7c4eedb146cbe7f95 is di5gva
plaintext of 21a47c906dbbe36e252921753864403e is sso55a
plaintext of 66e76fb30a7e59f1c9e4f748bbb09396 is tthela
plaintext of 855265960fecd55c76d5928c84b14886 is ofrora
plaintext of 189c2f65dfca3a7d44dbf967563a2051 is nizeda
plaintext of a9a2500b1222f6f0f16bf52455dfee7c is lou0ga
plaintext of b6b92809cafdb66e092476a53a085aa8 is opmena

statistics
----------------------------------------------------------------
plaintext found:                             11 of 15
total time:                                  4.55 s
time of chain traverse:                      3.39 s
time of alarm check:                         1.06 s
time of disk read:                           0.01 s
hash & reduce calculation of chain traverse: 108243000
hash & reduce calculation of alarm check:    33935224
number of alarm:                             34064
performance of chain traverse:               31.91 million/s
performance of alarm check:                  31.92 million/s

result
----------------------------------------------------------------
66e76fb30a7e59f1c9e4f748bbb09396  tthela  hex:747468656c61
1a10b176c926d5d6ea456117ac754533  tpoina  hex:74706f696e61
21a47c906dbbe36e252921753864403e  sso55a  hex:73736f353561
7f80e6d582cb2a18a2fe0b83d3afe830  <not found>  hex:<not found>
b6b92809cafdb66e092476a53a085aa8  opmena  hex:6f706d656e61
855265960fecd55c76d5928c84b14886  ofrora  hex:6f66726f7261
189c2f65dfca3a7d44dbf967563a2051  nizeda  hex:6e697a656461
b8f9c9311827bf24de109c4ed5447b0b  mlhdia  hex:6d6c68646961
a9a2500b1222f6f0f16bf52455dfee7c  lou0ga  hex:6c6f75306761
b95fdd0f9f4fe555a4e7b19d18117d60  <not found>  hex:<not found>
bcd8d08cfe9c57ecc5b9fd4b45d8be77  egunba  hex:6567756e6261
7cc7fdaf74697df714b383e34071b618  dsmtoa  hex:64736d746f61
39c7bc504190c8b7c4eedb146cbe7f95  di5gva  hex:646935677661
dee536e9130e8cc2550fed9e9b03a5a3  <not found>  hex:<not found>
7730e6289fc772646d5984c96c446e8f  <not found>  hex:<not found>
```

## Generation: 180,000 Entries

```
rainbowcrack-1.7-win64>rtgen.exe md5 loweralpha-numeric 6 6 0 3800 1800000 0
rainbow table md5_loweralpha-numeric#6-6_0_3800x1800000_0.rt parameters
hash algorithm:         md5
hash length:            16
charset name:           loweralpha-numeric
charset data:           abcdefghijklmnopqrstuvwxyz0123456789
charset data in hex:    61 62 63 64 65 66 67 68 69 6a 6b 6c 6d 6e 6f 70 71 72 73 74 75 76 77 78 79 7a 30 31 32 33 34 35 36 37 38 39
charset length:         36
plaintext length range: 6 - 6
reduce offset:          0x00000000
plaintext total:        2176782336

sequential starting point begin from 0 (0x0000000000000000)
generating...
262144 of 1800000 rainbow chains generated (0 m 28.6 s)
524288 of 1800000 rainbow chains generated (0 m 31.2 s)
786432 of 1800000 rainbow chains generated (0 m 31.0 s)
1048576 of 1800000 rainbow chains generated (0 m 32.9 s)
1310720 of 1800000 rainbow chains generated (0 m 31.7 s)
1572864 of 1800000 rainbow chains generated (0 m 31.7 s)
1800000 of 1800000 rainbow chains generated (0 m 32.2 s)
```

## Cracking

```
rainbowcrack-1.7-win64>rcrack.exe ./ -l salted6.txt
1 rainbow tables found
memory available: 1079771136 bytes
memory for rainbow chain traverse: 60800 bytes per hash, 912000 bytes for 15 hashes
memory for rainbow table buffer: 2 x 28800016 bytes
disk: ./\md5_loweralpha-numeric#6-6_0_3800x1800000_0.rt: 28800000 bytes read
disk: finished reading all files
plaintext of 1a10b176c926d5d6ea456117ac754533 is tpoina
plaintext of bcd8d08cfe9c57ecc5b9fd4b45d8be77 is egunba
plaintext of b8f9c9311827bf24de109c4ed5447b0b is mlhdia
plaintext of 7cc7fdaf74697df714b383e34071b618 is dsmtoa
plaintext of 7f80e6d582cb2a18a2fe0b83d3afe830 is owso9a
plaintext of 39c7bc504190c8b7c4eedb146cbe7f95 is di5gva
plaintext of 855265960fecd55c76d5928c84b14886 is ofrora
plaintext of a9a2500b1222f6f0f16bf52455dfee7c is lou0ga
plaintext of 21a47c906dbbe36e252921753864403e is sso55a
plaintext of 66e76fb30a7e59f1c9e4f748bbb09396 is tthela
plaintext of 189c2f65dfca3a7d44dbf967563a2051 is nizeda
plaintext of dee536e9130e8cc2550fed9e9b03a5a3 is cancea
plaintext of 7730e6289fc772646d5984c96c446e8f is aseasa
plaintext of b6b92809cafdb66e092476a53a085aa8 is opmena

statistics
----------------------------------------------------------------
plaintext found:                             14 of 15
total time:                                  5.09 s
time of chain traverse:                      3.97 s
time of alarm check:                         1.08 s
time of disk read:                           0.02 s
hash & reduce calculation of chain traverse: 108243000
hash & reduce calculation of alarm check:    31140517
number of alarm:                             38149
performance of chain traverse:               27.27 million/s
performance of alarm check:                  28.83 million/s

result
----------------------------------------------------------------
66e76fb30a7e59f1c9e4f748bbb09396  tthela  hex:747468656c61
1a10b176c926d5d6ea456117ac754533  tpoina  hex:74706f696e61
21a47c906dbbe36e252921753864403e  sso55a  hex:73736f353561
7f80e6d582cb2a18a2fe0b83d3afe830  owso9a  hex:6f77736f3961
b6b92809cafdb66e092476a53a085aa8  opmena  hex:6f706d656e61
855265960fecd55c76d5928c84b14886  ofrora  hex:6f66726f7261
189c2f65dfca3a7d44dbf967563a2051  nizeda  hex:6e697a656461
b8f9c9311827bf24de109c4ed5447b0b  mlhdia  hex:6d6c68646961
a9a2500b1222f6f0f16bf52455dfee7c  lou0ga  hex:6c6f75306761
b95fdd0f9f4fe555a4e7b19d18117d60  <not found>  hex:<not found>
bcd8d08cfe9c57ecc5b9fd4b45d8be77  egunba  hex:6567756e6261
7cc7fdaf74697df714b383e34071b618  dsmtoa  hex:64736d746f61
39c7bc504190c8b7c4eedb146cbe7f95  di5gva  hex:646935677661
dee536e9130e8cc2550fed9e9b03a5a3  cancea  hex:63616e636561
7730e6289fc772646d5984c96c446e8f  aseasa  hex:617365617361
```

## Generate and Crack: 30,000,000

```
D:\rainbowcrack-1.7-win64>rtgen.exe md5 loweralpha-numeric 6 6 0 3800 3000000 0
rainbow table md5_loweralpha-numeric#6-6_0_3800x3000000_0.rt parameters
hash algorithm:         md5
hash length:            16
charset name:           loweralpha-numeric
charset data:           abcdefghijklmnopqrstuvwxyz0123456789
charset data in hex:    61 62 63 64 65 66 67 68 69 6a 6b 6c 6d 6e 6f 70 71 72 73 74 75 76 77 78 79 7a 30 31 32 33 34 35 36 37 38 39
charset length:         36
plaintext length range: 6 - 6
reduce offset:          0x00000000
plaintext total:        2176782336

sequential starting point begin from 0 (0x0000000000000000)
generating...
262144 of 3000000 rainbow chains generated (0 m 32.6 s)
524288 of 3000000 rainbow chains generated (0 m 33.6 s)
786432 of 3000000 rainbow chains generated (0 m 33.0 s)
1048576 of 3000000 rainbow chains generated (0 m 34.6 s)
1310720 of 3000000 rainbow chains generated (0 m 35.8 s)
1572864 of 3000000 rainbow chains generated (0 m 34.6 s)
1835008 of 3000000 rainbow chains generated (0 m 37.0 s)
2097152 of 3000000 rainbow chains generated (0 m 34.3 s)
2359296 of 3000000 rainbow chains generated (0 m 32.5 s)
2621440 of 3000000 rainbow chains generated (0 m 38.2 s)
2883584 of 3000000 rainbow chains generated (0 m 36.2 s)
3000000 of 3000000 rainbow chains generated (0 m 17.7 s)

D:\rainbowcrack-1.7-win64>rtsort.exe .
.\md5_loweralpha-numeric#6-6_0_3800x1800000_0.rt:
1641742336 bytes memory available
loading data...
sorting data...
writing sorted data...

.\md5_loweralpha-numeric#6-6_0_3800x3000000_0.rt:
1611546624 bytes memory available
loading data...
sorting data...
writing sorted data...


D:\rainbowcrack-1.7-win64>rcrack.exe ./ -l salted6.txt
1 rainbow tables found
memory available: 1265454284 bytes
memory for rainbow chain traverse: 60800 bytes per hash, 912000 bytes for 15 hashes
memory for rainbow table buffer: 2 x 48000016 bytes
disk: ./\md5_loweralpha-numeric#6-6_0_3800x3000000_0.rt: 48000000 bytes read
disk: finished reading all files
plaintext of a9a2500b1222f6f0f16bf52455dfee7c is lou0ga
plaintext of 1a10b176c926d5d6ea456117ac754533 is tpoina
plaintext of bcd8d08cfe9c57ecc5b9fd4b45d8be77 is egunba
plaintext of b8f9c9311827bf24de109c4ed5447b0b is mlhdia
plaintext of 7cc7fdaf74697df714b383e34071b618 is dsmtoa
plaintext of 7f80e6d582cb2a18a2fe0b83d3afe830 is owso9a
plaintext of 39c7bc504190c8b7c4eedb146cbe7f95 is di5gva
plaintext of 855265960fecd55c76d5928c84b14886 is ofrora
plaintext of b6b92809cafdb66e092476a53a085aa8 is opmena
plaintext of 21a47c906dbbe36e252921753864403e is sso55a
plaintext of 66e76fb30a7e59f1c9e4f748bbb09396 is tthela
plaintext of 189c2f65dfca3a7d44dbf967563a2051 is nizeda
plaintext of 7730e6289fc772646d5984c96c446e8f is aseasa
plaintext of dee536e9130e8cc2550fed9e9b03a5a3 is cancea
plaintext of b95fdd0f9f4fe555a4e7b19d18117d60 is hed4ea

statistics
----------------------------------------------------------------
plaintext found:                             15 of 15
total time:                                  4.41 s
time of chain traverse:                      3.38 s
time of alarm check:                         0.94 s
time of disk read:                           0.03 s
hash & reduce calculation of chain traverse: 108243000
hash & reduce calculation of alarm check:    27986034
number of alarm:                             49664
performance of chain traverse:               32.06 million/s
performance of alarm check:                  29.84 million/s

result
----------------------------------------------------------------
66e76fb30a7e59f1c9e4f748bbb09396  tthela  hex:747468656c61
1a10b176c926d5d6ea456117ac754533  tpoina  hex:74706f696e61
21a47c906dbbe36e252921753864403e  sso55a  hex:73736f353561
7f80e6d582cb2a18a2fe0b83d3afe830  owso9a  hex:6f77736f3961
b6b92809cafdb66e092476a53a085aa8  opmena  hex:6f706d656e61
855265960fecd55c76d5928c84b14886  ofrora  hex:6f66726f7261
189c2f65dfca3a7d44dbf967563a2051  nizeda  hex:6e697a656461
b8f9c9311827bf24de109c4ed5447b0b  mlhdia  hex:6d6c68646961
a9a2500b1222f6f0f16bf52455dfee7c  lou0ga  hex:6c6f75306761
b95fdd0f9f4fe555a4e7b19d18117d60  hed4ea  hex:686564346561
bcd8d08cfe9c57ecc5b9fd4b45d8be77  egunba  hex:6567756e6261
7cc7fdaf74697df714b383e34071b618  dsmtoa  hex:64736d746f61
39c7bc504190c8b7c4eedb146cbe7f95  di5gva  hex:646935677661
dee536e9130e8cc2550fed9e9b03a5a3  cancea  hex:63616e636561
7730e6289fc772646d5984c96c446e8f  aseasa  hex:617365617361
```