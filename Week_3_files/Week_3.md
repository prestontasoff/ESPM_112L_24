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

As you can see, different assemblers win out over others when looking at particular metrics, but none is consistently better every time on all metrics. Different scenarios call for different assembly software. MEGAHIT, for example, is quite memory efficient. If your computer is lacking in RAM, or your data is quite large, MEGAHIT can make assembly possible where it was previously infeasible due to memory constraints.
It’s up to you to decide which one is best for your particular situation, based on the particular traits of each assembler (which are well described in the Vollmers et al. paper above).
We can see the effect of using different assemblers on our data, too. I ran megahit and metaSPAdes for one of our class examples, Cow_8_05. Here’s what the stats look like in comparison:
 
| Assembly Statistic           | MEGAHIT  | metaSPAdes |
| ---------------------------- | -------- | ---------- |
| # Contigs                    | 679,859  | 2,448,126  |
| N50                          | 1231 bp  | 578 bp     |
| Average Sequence Length      | 901.35 bp| 453.59 bp  |
| Largest Contig               | 429,190  | 502,671    |

 
Our lab uses either `metaSPAdes`, `idba_ud`, or `MEGAHIT`.

---

# Review: Quality and Trimming

- Last week, as you'll recall, we looked at how to investigate the quality of your reads with [FastQC](https://github.com/s-andrews/FastQC), as well as how to trim your reads based on quality using [bbduk](https://jgi.doe.gov/data-and-tools/software-tools/bbtools/bb-tools-user-guide/bbduk-guide/).

- Since we subset the reads last time due to computational constraints, I've provided two example FastQC reports for you: One pre-trimming and one post-trimming. They're stored at`/home/ptasoff/raw.d`. Try opening them with your browser and pulling them up side-by-side. What are the main differences you see? How dramatic is the difference in quality? (They shouldn't be terribly different)

---

# This week's material: Assembly and Assembly Statistics

# Section 1: Assembly

## First, we're going to set up a practice assembly. Navigate to `//class_data/practice_assembly/completed_assembly` and take a look at what's there. 

You'll notice there's two types of files here: `.fastq` and `.fa`. The `.fa` files are FASTA format, whereas the `.fastq` are in FASTQ format. You'll often see FASTA files with extensions like `.fa`, `.fasta`, `.fna`, and `.faa`. These all mean mostly the same thing, which is that it's in FASTA format. However, two are more specific: `fna` stands for **f**asta **n**ucleic **acid** (DNA FASTA) and `faa` stands for **f**asta **a**mino **a**cid (Protein FASTA).


Now you're going to be practicing genome assembly. You have two options here: assemble your `.fastq` files with `MEGAHIT`, or assemble your `.fa` file with `idba_ud`. Choose one and stick with it! I'll give you help below.

## Subsection: Tmux
This is going to take a super long time to run, so you're not gonna want to have one terminal window open the whole time. Allow me to teach you about a nifty program called `tmux`.

`tmux` allows you to make terminal windows that you can leave running (even when you close your connection!) and come back to later. It's really nice. There are other alternatives in bash, such as `nohup` and `screen`, but let's focus on this for now.


- You're going to want to make a new window before you start anything. Try this:

    - ```tmux new -s assembly```
    
- Congrats! Now you're in a new `tmux` window called 'assembly'. To exit this window and leave it running, press `CTRL+b`, then `d`. If you've done that and you want to get back, use:

   - ```tmux attach -t assembly```
   

# IMPORTANT: Only one person per group should do the rest of this section!

## Subsection: Assembly prep

Now we're going to prepare to run an assembly. Choose your reads, and do the following:

**If you're going to assemble .fastq files using MEGAHIT:**
- ```ln -s /class_data/practice_assembly/*.fastq ~```

**If you're going to assemble .fa files using idba_ud:**
- ```ln -s /class_data/practice_assembly/*.fasta ~```

This will create what's called a *symbolic link* in your home directory (~) - it's like copying over a file, but you don't actually make a new copy. You can just see the filename and operate on it as if you had copied it. If you remove this link, the original will be safe and sound in its original directory.

## The assembly command

Now, we're going to do actual assembly. Remember, **only one person per group should execute one of the following commands! We only have so many compute resources.**

I also highly encourage you to look into potential alterations to these commands, of which there are many. The commands I provided to you will work, but try using either of the following commands to see more parameters to play with, and please ask me about them in class! (The following commands show the help menus for these two assemblers.)

(don't play with the number of threads though)

This navigates to your home directory:
`cd ~`

#And this is to show the help page:
`idba_ud -h`

or for Megahit:

`megahit -h`

So you’re going to need at least two things to run the assembler:
-Reads to assemble (your `fastq` or `fasta` files)
-The name of an output directory

Here’s how to do that:


### First, make your output directory

#### If you're assembling using `idba_ud` and only for idba_ud (if not skip this step):
```mkdir ~/assembly```

Then do:

```idba_ud --pre_correction --min_contig 500 -r merged_reads.fasta --num_threads 4 -o ~/assembly```

#### If you're assembling using `megahit`, no need to make an output directory as it makes one already:
```megahit -1 /class_data/practice_assembly/Cow_8_05_trim_clean.PE.1.fastq -2 /class_data/practice_assembly/Cow_8_05_trim_clean.PE.2.fastq -o ~/assembly --num-cpu-threads 4 -m 0.13```

(The `-m 0.13` flag limits the process to 13% of the system's memory, ensuring that we can run at least 7 of these assemblies on the server at once.)

Now these should take about 20 minutes for `idba_ud` and 4 minutes for `MEGAHIT`.

---

# Section 2: Assembly Statistics


We’re going to use a script called `contig_stats.pl`, written in perl, to generate assembly statistics.

Navigate to your output directory (e.g. `cd ~/assembly`), and take a look at the files generated. 
If you did not do the assembly in your group, take a look at the directory for the pre-made assemblies (`/class_data/practice_assembly/completed_assembly`). *If you don't remember this ask me for help!*


You’ll notice a lot of different unfamiliar files, but two that should hopefully stand out: `contig.fa` and `scaffold.fa`. We want `scaffold.fa` - remember, contigs are stitched together to make scaffolds.

Let’s run contig_stats.pl to get a good idea of how well the assembly ran-

```
#This command will generate a file called 'scaffolds.contigstats.summary.txt
mkdir ~/contig_stats
contig_stats.pl -i scaffold.fa -o ~/contig_stats/scaffolds.contigstats
```

Let’s look now at the resulting contig stats- try `less ~/contig_stats/scaffolds.contigstats.summary.txt`. You’ll see something like this:

```
Length distribution
===================

Range    	# sequences (%)	# bps (%)
0-100:  	190 (0.24%)	14076 (0.04%)
100-500:  	65811 (83.44%)	17993525 (60.05%)
500-1000:  	10091 (12.79%)	6788583 (22.65%)
1000-5000:  	2694 (3.41%)	4317525 (14.4%)
5000-10000:  	70 (0.08%)	459324 (1.53%)
10000-20000:  	11 (0.01%)	144408 (0.48%)
20000-50000:  	3 (0%)	81549 (0.27%)
50000-:     	2 (0%)	163131 (0.54%)

General Information
==================

Total number of sequences: 78872
Total number of bps:       29962121
Average sequence length:   379.88 bps.
N50:                       364 bps
```



## Interpreting assembly statistics
Important stats to remember are:
•	N50 (Median contig size; half of contigs are above this size, half below)
•	Average sequence length
•	Total number of sequences (you want fewer, larger contigs!)
•	Number of large (50,000+ bp) contigs
### Getting assembly statistics for your sample
•	Take a look at the assembly directory (e.g. `/class_data/assemblies/Cow_8_05_idba_ud` or your own ~/assembly). 
•	Using the procedure above, generate contig stats for your scaffold file (scaffold.fa).
# Questions for today’s turn-in:
1.	What is the N50 of the contigs (not the scaffolds) from the example assembly? (Go back and repeat the procedure to run `contig_stats.pl` on the scaffolds from the example assembly, but choose `contig.fa` instead of `scaffold.fa`) 5pts
2.	What differentiates contigs from scaffolds? Should an assembly yield more scaffolds than contigs, or vice versa? 3pts
3.	What is the length of the largest contig in your sample’s idba_ud assembly? 2pts
4.	Provide the path (file location) of your example assembly output. 10pts
---

You did it!

![You get a genome!](https://i1.wp.com/i.imgflip.com/v80vq.jpg?resize=640%2C359&ssl=1)


(PC: https://www.molecularecologist.com/2015/12/post-holiday-gift-ideas-a-draft-genome/)
![image](https://github.com/prestontasoff/ESPM_112L_24/assets/116195371/bc5dc0e9-4780-4787-881f-236bd8f29c7d)
