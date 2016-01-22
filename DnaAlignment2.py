'''
DNA Alignment
Smith-Waterman Exercises (Local Alignments)

1. Two random sequences must be provided to the students.
2. A standard scoring system needs to be shown to the students. Example: +2 for a match, -1 for a mismatch, -2 for a gap.
'''

def sequenceAlign(seqA, seqB):

    DNA = {'G': { 'G':2, 'C':-1, 'A':-1, 'T':-1 },
           'C': { 'G':-1, 'C':2, 'A':-1, 'T':-1 },
           'A': { 'G':-1, 'C':-1, 'A':2, 'T':-1 },
           'T': { 'G':-1, 'C':-1, 'A':-1, 'T':2 }}
    
    numI = len(seqA) + 1
    numJ = len(seqB) + 1
    scoreMatrix = [[0] * numJ for x in range(numI)]             # Initiate scoreMatrix and routeMatrix, all 0
    routeMatrix = [[0] * numJ for x in range(numI)]
    maxN = 0
    
    for i in range(1, numI):
        for j in range(1, numJ):
            gapPenalty = -2                                     # -2 for gap
            similarity = DNA[seqA[i - 1]][seqB[j - 1]]          # +2 for match, -1 for dismatch
            paths = [scoreMatrix[i - 1][j - 1] + similarity,
                     scoreMatrix[i - 1][j] + gapPenalty,
                     scoreMatrix[i][j - 1] + gapPenalty]
            best = max(paths)
            route = paths.index(best)
            scoreMatrix[i][j] = max(best, 0)

            if scoreMatrix[i][j] >= maxN:
                maxN = scoreMatrix[i][j]                        # store the index of the maxNumber in the scoreMatrix
                k = i
                m = j

            routeMatrix[i][j] = route
            
    score = scoreMatrix[k][m]                                   # store the score

    alignA = []
    alignB = []

    i = k
    j = m
    
    while (i > 0 or j > 0) and scoreMatrix[i][j] != 0:          # Traceback
        route = routeMatrix[i][j]
        if route == 0:                                          # that score comes from diagonal
            alignA.append(seqA[i - 1])
            alignB.append(seqB[j - 1])
            i -= 1
            j -= 1
        if route == 1:                                          # that score comes from horizon, gap in seqB
            alignA.append(seqA[i - 1])
            alignB.append('-')
            i -= 1
        if route == 2:                                          # that score comes from vertical, gap in seqA
            alignA.append('-')
            alignB.append(seqB[j - 1])
            j -= 1
    alignA.reverse()
    alignB.reverse()
    alignA = ''.join(alignA)
    alignB = ''.join(alignB)

    return score, alignA, alignB

score, alignA, alignB = sequenceAlign('GGCTCAATCA', 'ACCTAAGG')


print(score)
print(alignA)

sign = []                                                       # print the '|' sign for alignment link
for i in range(0, len(alignA)):
    if alignA[i] == alignB[i]:
        sign.append('|')
    else:
        sign.append(' ')
sign = ''.join(sign)
print(sign)

print(alignB)
        
