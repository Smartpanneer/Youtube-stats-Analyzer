import requests
import streamlit as st

API_KEY='AIzaSyALH38iNTX89UrD9ow8mfProvh_JMXyXbg'

def get_channel_stats(channel_id):
    url=f"https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id={channel_id}&key={API_KEY}"
    responce=requests.get(url)
    data=responce.json()

    if 'items' not in data or not data['items']:
       return None
    item=data['items'][0]
    stats={'Channel_name':item['snippet']['title'],
           'Subscribers':item['statistics']['subscriberCount'],
           'Total views':item['statistics']['viewCount'],
           'Total video':item['statistics']['videoCount'],
           'Description':item['snippet']['description']}
    return stats
def main():
    st.title('Youtube channel stats analyzer')
    channel_id=st.text_input('Enter the youtube channel id: ')
    if st.button('Enter the button'):
        if channel_id:
            stats = get_channel_stats(channel_id)
            if stats:
                st.success("Channel data fetched successfully!")
                st.write(stats)
            else:
                st.error("Channel not found. Please check the ID.")
        else:
            st.warning("Please enter a channel ID.")
if __name__ == "__main__":
    main()

