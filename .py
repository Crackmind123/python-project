import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_csv(r"C:\Users\niloy\Downloads\Zomato data .csv")
df=pd.DataFrame(data)
#print(df.isnull().sum())   * no null values

df['rate'] = df['rate'].astype(str)
df['rate'] = df['rate'].apply(lambda x: x.split('/')[0].strip())
df['rate'] = df['rate'].replace(['NEW', '-', 'nan'], None)
df['rate'] = pd.to_numeric(df['rate'], errors='coerce')
df['approx_cost(for two people)']=pd.to_numeric(df['approx_cost(for two people)'],errors='coerce')
print(df)

plt.figure(figsize=(8,5))
sns.histplot(df['rate'].dropna(),bins=20,kde=True,color='blue')
plt.title('Distribution of resturant ratings')
plt.xlabel('Ratings')
plt.ylabel("No of restraunts")
plt.grid(True)
plt.show()

print("Skewness of Ratings:", df['rate'].skew())

type_count=df['listed_in(type)'].value_counts()
print(type_count.head(10))

type_count.head(10).plot(kind='bar',color='green')
plt.title('Top 10 restraunts')
plt.xlabel('Restraurant types')
plt.ylabel('no. of restraunts')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

av_rating_bytype=df.groupby('listed_in(type)')['rate'].mean().sort_values(ascending=False)
print(av_rating_bytype.head(10))
av_rating_bytype.head(10).plot(kind='barh', color='blue')
plt.title('Top Restaurant Types by Average Rating')
plt.xlabel('Average Rating')
plt.ylabel('Restaurant Type')
plt.tight_layout()
plt.show()

av_votes_bytype=df.groupby('listed_in(type)')['votes'].mean().sort_values(ascending=False)
print(av_votes_bytype.head(10))
av_votes_bytype.head(10).plot(kind='barh', color='purple')
plt.title('Top Restaurant Types by Average Votes')
plt.xlabel('Average Votes')
plt.ylabel('Restaurant Type')
plt.tight_layout()
plt.show()
order_vs_rate=df.groupby('online_order')['rate'].mean()
print("Rate by order type:",order_vs_rate)
order_va_vote=df.groupby('online_order')['votes'].mean()
print("Vote by order type:",order_va_vote)
# so online order increases the vote by 7 x times

print(df.groupby('book_table')['rate'].mean())
print(df.groupby('book_table')['votes'].mean())
#booking a table increases the rating and votes

rating_combo = df.groupby(['online_order', 'book_table'])['rate'].mean().unstack()
print(rating_combo)


rating_combo.plot(kind='bar', figsize=(8,5), color=['tomato', 'mediumseagreen'])
plt.title('Average Rating by Online Order & Table Booking')
plt.xlabel('Online Order')
plt.ylabel('Average Rating')
plt.ylim(0, 5)
plt.legend(title='Table Booking')
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(x='approx_cost(for two people)', y='votes', data=df, alpha=0.6, color='teal')
plt.title('Votes vs Approximate Cost for Two People')
plt.xlabel('Approximate Cost for Two People (₹)')
plt.ylabel('Number of Votes')
plt.grid(True)
plt.tight_layout()
plt.show()

print("Average cost of dinning for two people:",df['approx_cost(for two people)'].mean())

correlation=df[['approx_cost(for two people)','rate']].corr()
print("corelation between cost and rating:",correlation)
#low positive correlation 0.275216

plt.figure(figsize=(8,5))
sns.scatterplot(x='approx_cost(for two people)',y='rate',data=df,alpha=0.6)
plt.title('Cost vs Rating')
plt.xlabel("Cost")
plt.ylabel('Rating')
plt.grid(True)
plt.tight_layout()
plt.show()

cost_by_type=df.groupby('listed_in(type)')['approx_cost(for two people)'].mean().sort_values(ascending=False)
print('Average cost of restraurants by type:',cost_by_type)

corr=df[['votes','rate']].corr()
print("Correlation between votes and ratings:",corr)     #Correlation = 0.49 → This is a moderate positive correlation.


corr_analysis=df[['rate','votes','approx_cost(for two people)']].corr()
print("Correlation between rating,votes and cost:",corr_analysis)

plt.figure(figsize=(6, 4))
sns.heatmap(corr_analysis, annot=True, cmap='YlGnBu', fmt=".2f", linewidths=0.5)
plt.title('Correlation Heatmap: Rating, Votes & Cost')
plt.tight_layout()
plt.show()


top_10_rated = df.sort_values(by='rate', ascending=False).dropna(subset=['rate']).head(10)
print(top_10_rated[['name', 'rate', 'approx_cost(for two people)', 'votes']])
avg_cost_top10 = top_10_rated['approx_cost(for two people)'].mean()
avg_votes_top10 = top_10_rated['votes'].mean()

print("Average cost for Top 10 rated restaurants: ₹", round(avg_cost_top10, 2))       #Average cost for Top 10 rated restaurants: ₹ 595.0
print("Average number of votes for Top 10 rated restaurants:", round(avg_votes_top10))      #Average number of votes for Top 10 rated restaurants: 1606

top_voted = df.sort_values(by='votes', ascending=False).dropna(subset=['rate']).head(10)
print(top_voted[['name', 'rate', 'votes', 'approx_cost(for two people)']])

avg_rating_top_voted = top_voted['rate'].mean()
print("Average rating of Top 10 most-voted restaurants:", round(avg_rating_top_voted, 2))

