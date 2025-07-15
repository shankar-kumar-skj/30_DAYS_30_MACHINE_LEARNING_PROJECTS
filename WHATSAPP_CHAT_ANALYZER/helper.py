from urlextract import URLExtract
import matplotlib.pyplot as plt
from wordcloud import WordCloud

extract=URLExtract()


def fetch_stats(selected_user,df):
    if selected_user !='Overall':
        df=df[df['user']==selected_user]

    num_message=df.shape[0]
    words=[]
    for message in df['message']:
        words.extend(message.split())

    # fetch number of media message
    num_media_message=df[df['message']=='<Media omitted>\n'].shape[0]

    # fetch number of links shared
    links=[]
    for message in df['message']:
        links.extend(extract.find_urls(message))

    return num_message,len(words),num_media_message,len(links)

def most_busy_user(df):
    x=df['user'].value_counts().head()
    df=round((df['user'].value_counts()/df.shape[0])*100,2).reset_index().rename(columns={'user':'name','count':'percent'})
    return x,df


def create_wordcloud(selected_user,df):
    if selected_user !='Overall':
        df=df[df['user']==selected_user]

    wc=WordCloud(width=500,height=500,min_font_size=10,background_color='white')
    df_wc=wc.generate(df['message'].str.cat(sep=" "))
    return df_wc

    # name=x.index
    # count=x.values
    # plt.bar(name,count)
    # plt.xticks(rotation='vertical')
    # plt.show()


    # if selected_user =='Overall':
    #     # 1. fetch number of messages
    #     num_message=df.shape[0]
    #     # 2. fetch number of words
    #     words=[]
    #     for message in df['message']:
    #         words.extend(message.split())

    #     return num_message,len(words)
    # else:
    #     new_df=df[df['user']==selected_user]
    #     num_message=new_df.shape[0]
    #     words=[]
    #     for message in new_df['message']:
    #         words.extend(message.split())
    #     return num_message,len(words)