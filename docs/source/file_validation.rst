===============
File validation
===============

File level validation
---------------------

==  ==============================================  =============
ID  Constraint                                      Failure level
==  ==============================================  =============
1   File should be readable                         ER
2   First record should be HDR                      ER
3   Second record should be GRH                     ER
4   Groups open with GRH and close with GRT         ER
5   Last record is TRL                              ER
6   GRH should be followed by a Transaction header  ER
7   GRT should be followed by a GRH or TRL          ER
7   Only a single HDR and a single TRL exist        ER
==  ==============================================  =============