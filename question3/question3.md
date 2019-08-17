## ***Question 3 - Create a subset array***

### A. Compute allele-frequency differential
One way to further filter down the number of markers chosen for the  
array is to use the samples similarity matrix (question 2 part 3) in order  
to split the available samples dataset into two populations.  
Each population group will hopefully contain samples sharing high number of  
markers between themselves.

Then we will be able to compare the allele-frequency differential between  
the two samples populations, as suggested in
 [\[1\]](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3864958/#pone.0082434-Lao1)
 [\[2\]](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1712479/).
 
The allele-frequency differential is computed for each allele type separately  
(usually the highest freq one). Markers showing large differential  
between the two populations are considered more informative,   
so markers with low differential can be filtered out.


### B. Splitting samples and markers based on Designation (Species)
#### I. Markers
As described on [TAMU CottonSNP63K](https://www.cottongen.org/data/community_projects/tamu63k)
webpage, The marker database  
hold "45,104 putative intra‐specific single nucleotide polymorphism (SNP)  
markers for use within the cultivated cotton species Gossypium hirsutum L.  
and 17,954 putative inter‐specific SNP markers for use with crosses of  
other cotton species"

Additional information from our client regarding the targeted species  
can help us exclude markers based on which cotton specie they better fit.

#### II. Samples
 
Using the samples designation in order to divide the samples  
dataset into sub population in a different way. Then compute The  
allele-frequency differential and filter markers as described earlier. 


### C. Filter markers based on heterozygous fraction

As question2 answer page shows, there a big group of 7500+ markers with  
considerably high number of heterozygous genotypes read (fraction >0.9)  
in comparision to the rest of the markers (fraction <0.1).  
 
Supposedly**,markers with high number of bi-allellic reads will provide  
less separation and information, making them candidates for exclusion.  
 

** My knowledge on DNA microarrays is limited, further research on this  
subject will offer a clear answer.
 


### Citations
1. Ozerov M, Vasemägi A, Wennevik V, et al. Finding markers that make a  
 difference: DNA pooling and SNP-arrays identify population informative  
  markers for genetic stock identification. PLoS One. 2013;8(12):e82434.  
   Published 2013 Dec 16. doi:10.1371/journal.pone.0082434
   
2. Shriver MD, Smith MW, Jin L, et al. Ethnic-affiliation estimation by  
 use of population-specific DNA markers. Am J Hum Genet.  
  1997;60(4):957–964.