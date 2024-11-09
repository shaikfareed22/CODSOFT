# Collaborative Filtering Example
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
data = {
    'user_id': [1, 1, 1, 2, 2, 3, 3, 3, 4, 4],
    'movie_id': [1, 2, 3, 1, 3, 2, 3, 4, 1, 2],
    'rating': [5, 3, 4, 4, 5, 2, 3, 4, 5, 2]    
    
}

df = pd.DataFrame(data)
user_item_matrix = df.pivot_table(index='user_id', columns='movie_id', values='rating').fillna(0)
user_similarity = cosine_similarity(user_item_matrix) # Compute Similarity Matrix
user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)
def get_recommendations(user_id, user_item_matrix, user_similarity_df, n_recommendations=3):  # Function to get recommendations
    similar_users = user_similarity_df[user_id].sort_values(ascending=False).index[1:]
    similar_users_ratings = user_item_matrix.loc[similar_users]
    # Weighted sum of ratings from similar users
    weighted_ratings = similar_users_ratings.T.dot(user_similarity_df[user_id][similar_users])
    recommendations = weighted_ratings[weighted_ratings > 0].sort_values(ascending=False)
    
    return recommendations.head(n_recommendations)
print("Collaborative Filtering Recommendations for User 1:") # Example: Get recommendations for user_id 1
print(get_recommendations(1, user_item_matrix, user_similarity_df))

#"install library:
# pip install pandas scikit-learn"
# run the code in a python environment.