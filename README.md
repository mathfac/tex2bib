tex2bib
=======

Converts LaTex bibitems to BibTex library format.

Examples
=======
Source:
```
 \bibitem{TAAC2012}  Maksymets O.M.
 \newblock Upper approximation method for polynomial invariants
 \newblock Theoretical and Applied Aspects of Cybernetics. Proceedings of the
 2nd International Scientific Conference of Students and Young Scientists. Computer Science Section. -Kyiv: Bukrek.  - 2012. P. 45-47.
```

Result:
```
 @ARTICLE{TAAC2012,
 author       = "O. M. Maksymets",
 title        = "Upper approximation method for polynomial invariants",
 journal      = "Theoretical and Applied Aspects of Cybernetics. Proceedings of the 2-nd International Scientific Conference of Students and Young Scientists. Computer Science Section.",
 year         = "2012",
 pages        = "45--47",
 address      =  "Kyiv",
 language     = "english"
 }
 ```
