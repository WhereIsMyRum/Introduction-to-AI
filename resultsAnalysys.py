import numpy as np
from sklearn import preprocessing as pr
import matplotlib.pylab as plt


# the order of game scores array (starting algorithm)
# Random,  MCTS,  MM2, MM5, MM7, MM9,

scores_against_rand = [44, 99,  100,  97, 99, 96]
scores_against_mm2 = [4, 63, 94, 86, 91, 3]
scores_against_mm5 = [4, 38, 84, 82, 90, 2]
scores_against_mm7 = [2,  5, 36, 82, 82, 9]
scores_against_mm9 = [0, 29, 75, 89, 82, 8]
scores_against_mcts = [2, 99, 96, 100,  100, 53]

score_matrix = [scores_against_rand, scores_against_mcts, scores_against_mm2, scores_against_mm5, scores_against_mm7, scores_against_mm9]
score_matrix = np.asarray(score_matrix)
print(score_matrix.shape)

# comparison of pruning / no pruning order
# mm2, mm4, mm5, mm6, mm7, mm8, mm9, mm10
max_depth = [5,6,7,8,9]#,10]
pruning_states = (2210, 8389, 33162, 127515, 473494)# 1729014)
pruning_time = (0.0307, 0.0914, 0.3976,  1.5291, 6.1198)#, 19.9147)

nopruning_states = (5859, 29092, 143522, 706577, 3470067)# 16989674)
nopruning_time = (0.0515, 0.3447, 1.3731, 6.9348, 33.1439)#, 191.1332)


#normalized_pruning_states = pr.normalize((pruning_states))
#normalized_pruning_time = pr.normalize([pruning_time])

#normalized_nopruning_states = pr.normalize((nopruning_states))
#normalized_nopruning_time = pr.normalize([nopruning_time])

fig, ax = plt.subplots()
index = np.arange(len(max_depth))
bar_width = 0.3

opacity = 0.4

rects1 = ax.bar(index, pruning_states, bar_width, alpha=opacity, color='b', label="pruning")
rects2 = ax.bar(index + bar_width, nopruning_states, bar_width, alpha=opacity, color='r', label="no pruning")

ax.set_xlabel('Max depth')
ax.set_ylabel('Number of states')
ax.set_title('No. of states by max depth and pruning')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(('2','4','5','6','7','8','9','10'))
ax.legend()

fig2, ax2 = plt.subplots()

rects1 = ax2.bar(index, pruning_time, bar_width, alpha=opacity, color='b', label="pruning")
rects2 = ax2.bar(index + bar_width, nopruning_time, bar_width, alpha=opacity, color='r', label="no pruning")

ax2.set_xlabel('Max depth')
ax2.set_ylabel('Runtime')
ax2.set_title('Runtime by max depth and pruning')
ax2.set_xticks(index + bar_width / 2)
ax2.set_xticklabels(('2','4','5','6','7','8','9','10'))
ax2.legend()

fig2.tight_layout()


fig3, ax3 = plt.subplots()
min_val, max_val = 0,100
im = ax3.matshow(score_matrix, cmap=plt.cm.Reds)
ax3.set_xticklabels(('rand', 'rand','mcts','mm2','mm5','mm7','mm9'))
ax3.set_yticklabels(('rand',  'rand','mcts','mm2','mm5','mm7','mm9'))
fig3.colorbar(im)
fig3.tight_layout()
plt.show()