# Welcome to Week 3 lab!

## This week we're going to be looking at metagenome assembly- what it is, how to do it, and best practices.

## Your samples are enormous (some of the .fastq files are >65GB!) so we're not going to be able to do metagenome assembly on all of these today.

## What we are going to do is an overview of metagenome assembly- what it is, how to run it, and what software to use.

### First, [here's a link](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0169662) to a nice review by Vollmers et al. that describes the most popular software packages for metagenome assembly. It'll be a nice resource for you in the future if you encounter this again.

### Second, let's go over the methods we use in our lab and why we use them.

Our lab uses `idba_ud`, as we tend to get the best results with it (and it has a nice built-in scaffolder). 
This is by no means a one-size-fits-all solution; different assemblers work to different degrees depending on the type of sample you're working with, its environment of origin, and your sequencing depth.

For a nice example, see the image below from the paper mentioned above:

<img src="https://journals.plos.org/plosone/article/figure/image?size=large&id=info:doi/10.1371/journal.pone.0169662.g002" width=500>

As you can see, different assemblers win out over others when looking at particular metrics, but none is consistently better than all the others based on all metrics across different sample types. 
It's up to you to decide which one is best for your particular situation, based on the particular traits of each assembler (which are well described in the Vollmers et al. paper above).

---

- Last week, as you'll recall, we looked at how to investigate the quality of your reads with [FastQC](https://github.com/s-andrews/FastQC), as well as how to trim your reads based on quality using [Sickle](https://github.com/najoshi/sickle).

- Since we subset the reads last time due to computational constraints, I've provided two example FastQC reports for you: One pre-trimming and one post-trimming. /home/jwestrob/fastqc_output/S3_002_pre_trimming_fastqc.html and /home/jwestrob/fastqc_output/S3_002_trimmed_fastqc.html. They're both also stored in this github repository. Try opening them with your browser and pulling them up side-by-side. What are the main differences you see?

- Take a look at the 
