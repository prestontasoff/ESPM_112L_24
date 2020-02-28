import os, sys
from Bio import SeqIO

clsfile = sys.argv[1]
baby_id = sys.argv[2]


#Parse names file
names_file = '/class_data/' + baby_id + '/esom_files/Tetra_esom_2500.names'
with open(names_file, 'r') as infile:
    names_lines = [x.rstrip().split('\t') for x in infile.readlines()][1:]



point_list = [x[0] for x in names_lines]
scaf_list = [x[2] for x in names_lines]

point2scaf = dict(zip(point_list, scaf_list))

#cls_lines = []
#Parse cls file
with open(clsfile, 'r') as infile:
    lines = [x.rstrip() for x in infile.readlines()]

bin_lines = [x[1:].split('\t') for x in filter(lambda x: x.startswith('%') and '\t' in x, lines)]

bins = [x[0] for x in bin_lines]

membership_lines = [x.split('\t') for x in filter(lambda x: not x.startswith('%'), lines)]

points = [x[0] for x in membership_lines]
point_bins = [x[1] for x in membership_lines]
point2bin  = dict(zip(points, point_bins))

scafs_and_bins = [['scaffold_name', 'organism_name', 'organism_taxonomy']]

for scaffold in scaf_list:
    #Get lines in names file corresponding to scaffold in question
    points_and_scafs = list(filter(lambda x: x[2] == scaffold, names_lines))

    #Get counts of all the bin memberships for each point along the contig
    scaf_points = [x[0] for x in points_and_scafs]
    scaf_bins = [point2bin[point] for point in scaf_points]

    bin_counts = [scaf_bins.count(x) for x in scaf_bins]

    #Find the bin with at least 50% of the votes and declare that scaffold to belong
    #to that bin

    winning_bin = -1
    num_points = float(len(points_and_scafs))

    for index, count in enumerate(bin_counts):
            if count >= num_points/2.0:
                winning_bin = scaf_bins[index]

    if int(winning_bin) >= 0:
        scafs_and_bins.append([scaffold, winning_bin, 'Unknown'])





with open(baby_id + '_ESOMbins.scaffold2bin.tsv', 'w') as outfile:
    for element in scafs_and_bins:
        outfile.writelines('\t'.join(element) + '\n')
