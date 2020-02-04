# Welcome to Week 3 of ESPM 112 lab!

## This week we're going to be looking at metagenome assembly- what it is, how to do it, and best practices.

## Your samples are enormous (some of the uncompressed .fastq files are >65GB!) so we're not going to be able to do metagenome assembly on all of these today.

## What we are going to do is an overview of metagenome assembly- what it is, how to run it, and what software to use.

### First, [here's a link](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0169662) to a nice paper by Vollmers et al. that describes the most popular software packages for metagenome assembly. It'll be a nice resource for you in the future if you encounter this again.

### Second, let's go over the methods we use in our lab and why we use them.

Our lab uses `idba_ud`, as we tend to get the best results with it (and it has a nice built-in scaffolder). 
This is by no means a one-size-fits-all solution; different assemblers work to different degrees depending on the type of sample you're working with, its environment of origin, and your sequencing depth.

For a nice example, see the image below from the paper mentioned above:

<img src="https://journals.plos.org/plosone/article/figure/image?size=large&id=info:doi/10.1371/journal.pone.0169662.g002" width=500>

As you can see, different assemblers win out over others when looking at particular metrics, but none is consistently better than all the others based on all metrics across different sample types. 
It's up to you to decide which one is best for your particular situation, based on the particular traits of each assembler (which are well described in the Vollmers et al. paper above).

---

# Review: Quality and Trimming

- Last week, as you'll recall, we looked at how to investigate the quality of your reads with [FastQC](https://github.com/s-andrews/FastQC), as well as how to trim your reads based on quality using [Sickle](https://github.com/najoshi/sickle).

- Since we subset the reads last time due to computational constraints, I've provided two example FastQC reports for you: One pre-trimming and one post-trimming. They're stored at`/home/jwestrob/fastqc_output/S3_002_pre_trimming_fastqc.html` and `/home/jwestrob/fastqc_output/S3_002_trimmed_fastqc.html`, and they're both also stored in this github repository. Try opening them with your browser and pulling them up side-by-side. What are the main differences you see? How dramatic is the difference in quality?

---

# This week's material: Assembly and Assembly Statistics

### First, we're going to set up a practice assembly. Navigate to `/class_data/practice_assembly` and take a look at what's there.


- You'll notice there's two types of files here: `.fastq` and `.fa`. The `.fa` files are FASTA format, whereas the `.fastq` are in FASTQ format. You'll often see FASTA files with extensions like `.fa`, `.fasta`, `.fna`, and `.faa`. These all mean mostly the same thing, which is that it's in FASTA format. However, two are more specific: `fna` stands for **f**asta **n**ucleic **acid** (DNA FASTA) and `faa` stands for **f**asta **a**mino **a**cid (Protein FASTA).
    - 

---
- Take a look at the directory for your sample (e.g. /class_data/S3_002_000X1 or similar). *If you don't remember this ask me for help!*

- You'll see two subfolders now - `assembly.d` and `raw.d`. We've already assembled this data, since it's absolutely enormous and would take a really long time to assemble on the class server. You'll find the reads you were working with last week in `raw.d` and the pre-made assemblies in `assembly.d`.

- We're going to do a little bit of post-assembly quality control using the scaffolds now, which is just as important as investigating the quality of the reads pre-assembly. 
