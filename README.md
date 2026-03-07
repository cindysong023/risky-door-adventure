# BCOG200 final project
BCOG200 final project
1. For my final project, I will create a simple apple snack game where the player moves around and chooses between two types of apples. One type of apple will always give a small, safe number of points. The other type of apple will sometimes give a large reward, but sometimes cause the player to lose points. The player must decide which apple to choose in order to earn the highest total score. 

2a. I plan to write a choose_action() function. This function will allow the player to choose between the safe apple and the risky apple each turn. It will take the player’s input and return which option was selected.

2b. I plan to write a get_reward(action) function. This function will determine how many points the player earns after choosing an apple. If the safe apple is chosen, it will always return a small reward. If the risky apple is chosen, it will randomly return either a large reward or a loss of points.

2c. I plan to write a update_score(reward) function. This function will update the player’s total score after each turn. It will add the reward to the current score or subtract points if there is a penalty.

