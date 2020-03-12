# Welcome to metagenomics data analysis lab week 8: Friday the 13th quarantine edition!

Hello everyone and welcome! This week's lab is going to be a bit shorter since we're transitioning to a newer format and I wanted to make sure that everything will go smoothly for this week. We can start doing more complex things again next week. 

This week's lab is going to be a demonstration/instruction of how to go about investigating interesting proteins you find in metagenomic data. Today we're going to focus exclusively on proteins you can find in your bins, since those are more interesting (you know, relatively, which organism they came from).

In our lab, we use several popular tools to look at interesting proteins, which each have their own advantages and disadvantages. Let's talk about them, and what they're each good at.

## Goals for today:

- Predict genes, ORFs using Prodigal
- Learn how to use BLASTp/BLASTn (your choice)
- Learn how to use Interpro and HMMscan
- Start playing with KEGG and investigating the metabolic pathways your proteins are part of

---

## Tools to investigate proteins of interest:

- Interproscan (most thorough)

<a href="https://www.ebi.ac.uk/interpro/search/sequence/">https://www.ebi.ac.uk/interpro/search/sequence/</a>

This option is the best if you have a protein that's really unusual and you want to find out exactly what it is. Interproscan uses a large suite of HMMs (probabilistic models that we won't go over in detail today)

