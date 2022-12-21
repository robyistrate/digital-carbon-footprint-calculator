import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

header = st.container()
user_input = st.container()
results = st.container()

with header:
    st.title('Digital Carbon Footprint Calculator')
    st.text('''
            Determine the climate impacts of your Internet consumption habits
            ''')

list_of_countries = ['Global', 'Brazil', 'Canada', 'China', 'India', 'United States', 'Norway',
                     'Switzerland', 'France', 'Denmark', 'Spain', 'Italy', 'Germany', 'Poland',
                     'United Kingdom', 'South Africa', 'Australia', 'Russia']

lca_data = pd.read_csv(r'data/lca_data_digital_content.csv')


with user_input:
    st.markdown("""---""")
    st.subheader('How much time do you spend on the Internet each day?')
    st.markdown('Introduce the daily time (in minutes) that you spend \
                on average consuming the following digital content:')

    c1, c2, c3, c4, c5 = st.columns(5)
    web_surfing_time = c1.number_input("Web surfing", value=120, min_value=0, max_value=24*60)
    social_media_time = c2.number_input("Social media", value=147, min_value=0, max_value=24*60)
    video_streaming_time = c3.number_input("Video streaming", value=137, min_value=0, max_value=24*60)
    music_streaming_time = c4.number_input("Music streaming", value=93, min_value=0, max_value=24*60)
    video_conferencing_time = c5.number_input("Video conferencing", value=34, min_value=0, max_value=24*60)
    sum_time = web_surfing_time + social_media_time + video_streaming_time + music_streaming_time + video_conferencing_time
    st.text('Daily time spend on the Internet: ' + str(round(sum_time/60,2)) + ' hours')

    # Devices prefernce
    st.subheader('What devices do you use to access the Internet?')
    st.markdown('Introduce the percentage of time that you use each device \
                to access digital content:')
    percentage_warming = 'Warning: Values does not sum 100% '

    st.markdown('**Web surfing**')
    c1, c2, c3, c4, c5, c6 = st.columns(6)
    web_surfing_smartphone = c2.slider('Smartphone', min_value=0, max_value=100, value=40, step=1, format="%d%%")
    web_surfing_tablet = c3.slider('Tablet', min_value=0, max_value=100, value=25, step=1, format="%d%%")
    web_surfing_laptop = c4.slider('Laptop', min_value=0, max_value=100, value=25, step=1, format="%d%%")
    web_surfing_desktop = c5.slider('Desktop PC', min_value=0, max_value=100, value=10, step=1, format="%d%%")

    sum_time = web_surfing_smartphone + web_surfing_tablet + web_surfing_laptop + web_surfing_desktop
    if sum_time != 100:
        st.text(percentage_warming + '(' + str(sum_time) + '%)')

    st.markdown('**Social media**')
    c1, c2, c3, c4, c5, c6 = st.columns(6)
    social_media_smartphone = c2.slider('Smartphone ', min_value=0, max_value=100, value=40, step=1, format="%d%%")
    social_media_tablet = c3.slider('Tablet ', min_value=0, max_value=100, value=25, step=1, format="%d%%")
    social_media_laptop = c4.slider('Laptop ', min_value=0, max_value=100, value=25, step=1, format="%d%%")
    social_media_desktop = c5.slider('Desktop PC ', min_value=0, max_value=100, value=10, step=1, format="%d%%")

    sum_time = social_media_smartphone + social_media_tablet + social_media_laptop + social_media_desktop
    if sum_time != 100:
        st.text(percentage_warming + '(' + str(sum_time) + '%)')

    st.markdown('**Video streaming**')
    c1, c2, c3, c4, c5, c6 = st.columns(6)
    video_smartphone = c2.slider('Smartphone  ', min_value=0, max_value=100, value=30, step=1, format="%d%%")
    video_tablet = c3.slider('Tablet  ', min_value=0, max_value=100, value=25, step=1, format="%d%%")
    video_laptop = c4.slider('Laptop  ', min_value=0, max_value=100, value=25, step=1, format="%d%%")
    video_desktop = c5.slider('Desktop PC  ', min_value=0, max_value=100, value=10, step=1, format="%d%%")
    video_tv = c6.slider('Television', min_value=0, max_value=100, value=10, step=1, format="%d%%")

    sum_time = video_smartphone + video_tablet + video_laptop + video_desktop + video_tv
    if sum_time != 100:
        st.text(percentage_warming + '(' + str(sum_time) + '%)')

    st.markdown('**Music streaming**')
    c1, c2, c3, c4, c5, c6 = st.columns(6)
    music_smartphone = c2.slider('Smartphone   ', min_value=0, max_value=100, value=40, step=1, format="%d%%")
    music_tablet = c3.slider('Tablet   ', min_value=0, max_value=100, value=25, step=1, format="%d%%")
    music_laptop = c4.slider('Laptop   ', min_value=0, max_value=100, value=25, step=1, format="%d%%")
    music_desktop = c5.slider('Desktop PC   ', min_value=0, max_value=100, value=10, step=1, format="%d%%")

    sum_time = music_smartphone + music_tablet + music_laptop + music_desktop
    if sum_time != 100:
        st.text(percentage_warming + '(' + str(sum_time) + '%)')

    st.markdown('**Video conferencing**')
    c1, c2, c3, c4, c5, c6 = st.columns(6)
    conferencing_laptop = c2.slider('Laptop    ', min_value=0, max_value=100, value=50, step=1, format="%d%%")
    conferencing_desktop = c3.slider('Desktop PC    ', min_value=0, max_value=100, value=50, step=1, format="%d%%")

    sum_time = conferencing_laptop + conferencing_desktop
    if sum_time != 100:
        st.text(percentage_warming + '(' + str(sum_time) + '%)')

    # Video streaming resolution
    st.subheader('What video streaming resolution do you use?')
    st.markdown('Introduce the percentage of time that you watch video at each streaming resolution:')

    c1, c2, c3, c4 = st.columns(4)
    video_480p = c1.slider('480p', min_value=0, max_value=100, value=0, step=1, format="%d%%")
    video_720p = c2.slider('720p', min_value=0, max_value=100, value=50, step=1, format="%d%%")
    video_1080p = c3.slider('1080p', min_value=0, max_value=100, value=50, step=1, format="%d%%")
    video_4k = c4.slider('4K', min_value=0, max_value=100, value=0, step=1, format="%d%%")

    sum_time = video_480p + video_720p + video_1080p + video_4k
    if sum_time != 100:
        st.text(percentage_warming + '(' + str(sum_time) + '%)')

    # Video conferencing setting
    st.subheader('What video conferencing setting do you use?')
    st.markdown('Introduce the percentage of time that you join online meetings with each setting:')

    c1, c2, c3, c4 = st.columns(4)
    conferencing_only_audio = c1.slider('Audio only', min_value=0, max_value=100, value=50, step=1, format="%d%%")
    conferencing_audio_and_video = c2.slider('Audio and video', min_value=0, max_value=100, value=50, step=1, format="%d%%")

    sum_time = conferencing_only_audio + conferencing_audio_and_video
    if sum_time != 100:
        st.text(percentage_warming + '(' + str(sum_time) + '%)')

    # User location
    st.subheader('Select your location')
    c1, c2 = st.columns(2)
    user_loc = c1.selectbox('*Choose "Global" if your country is not in the list*', 
                            options = sorted(list_of_countries), index=0)

    st.write("#")
    display_results = st.button('Calculate')

lca_data_location = lca_data[lca_data['Location'] == user_loc]

# Time spend converted to hours per year
web_surfing_time = web_surfing_time * (1/60) * 365
social_media_time = social_media_time * (1/60) * 365
video_streaming_time = video_streaming_time * (1/60) * 365
music_streaming_time = music_streaming_time * (1/60) * 365
video_conferencing_time = video_conferencing_time * (1/60) * 365


# Calculate carbon footprint by digital content
web_surfing_carbon_footprint = web_surfing_time * (web_surfing_smartphone/100 * lca_data_location[lca_data_location['Name'] == 'web surfing, smartphone']['Carbon footprint'].values[0] + 
                                                   web_surfing_tablet/100 * lca_data_location[lca_data_location['Name'] == 'web surfing, tablet']['Carbon footprint'].values[0] + 
                                                   web_surfing_laptop/100 * lca_data_location[lca_data_location['Name'] == 'web surfing, laptop']['Carbon footprint'].values[0] + 
                                                   web_surfing_desktop/100 * lca_data_location[lca_data_location['Name'] == 'web surfing, desktop computer']['Carbon footprint'].values[0])

social_media_carbon_footprint = social_media_time * (social_media_smartphone/100 * lca_data_location[lca_data_location['Name'] == 'social media, smartphone']['Carbon footprint'].values[0] + 
                                                   social_media_tablet/100 * lca_data_location[lca_data_location['Name'] == 'social media, tablet']['Carbon footprint'].values[0] + 
                                                   social_media_laptop/100 * lca_data_location[lca_data_location['Name'] == 'social media, laptop']['Carbon footprint'].values[0] + 
                                                   social_media_desktop/100 * lca_data_location[lca_data_location['Name'] == 'social media, desktop computer']['Carbon footprint'].values[0])

video_streaming_480p_carbon_footprint = video_streaming_time * video_480p/100 * (video_smartphone/100 * lca_data_location[lca_data_location['Name'] == 'video streaming, 480p, smartphone']['Carbon footprint'].values[0] + 
                                                                                video_tablet/100 * lca_data_location[lca_data_location['Name'] == 'video streaming, 480p, tablet']['Carbon footprint'].values[0] + 
                                                                                video_laptop/100 * lca_data_location[lca_data_location['Name'] == 'video streaming, 480p, laptop']['Carbon footprint'].values[0] + 
                                                                                video_desktop/100 * lca_data_location[lca_data_location['Name'] == 'video streaming, 480p, desktop computer']['Carbon footprint'].values[0] +
                                                                                video_tv/100 * lca_data_location[lca_data_location['Name'] == 'video streaming, 480p, television 720p']['Carbon footprint'].values[0])

video_streaming_720p_carbon_footprint = video_streaming_time * video_720p/100 * (video_smartphone/100 * lca_data_location[lca_data_location['Name'] == 'video streaming, 720p, smartphone']['Carbon footprint'].values[0] + 
                                                                                video_tablet/100 * lca_data_location[lca_data_location['Name'] == 'video streaming, 720p, tablet']['Carbon footprint'].values[0] + 
                                                                                video_laptop/100 * lca_data_location[lca_data_location['Name'] == 'video streaming, 720p, laptop']['Carbon footprint'].values[0] + 
                                                                                video_desktop/100 * lca_data_location[lca_data_location['Name'] == 'video streaming, 720p, desktop computer']['Carbon footprint'].values[0] +
                                                                                video_tv/100 * lca_data_location[lca_data_location['Name'] == 'video streaming, 720p, television 720p']['Carbon footprint'].values[0])

video_streaming_1080p_carbon_footprint = video_streaming_time * video_1080p/100 * (video_smartphone/100 * lca_data_location[lca_data_location['Name'] == 'video streaming, 1080p, smartphone']['Carbon footprint'].values[0] + 
                                                                                video_tablet/100 * lca_data_location[lca_data_location['Name'] == 'video streaming, 1080p, tablet']['Carbon footprint'].values[0] + 
                                                                                video_laptop/100 * lca_data_location[lca_data_location['Name'] == 'video streaming, 1080p, laptop']['Carbon footprint'].values[0] + 
                                                                                video_desktop/100 * lca_data_location[lca_data_location['Name'] == 'video streaming, 1080p, desktop computer']['Carbon footprint'].values[0] +
                                                                                video_tv/100 * lca_data_location[lca_data_location['Name'] == 'video streaming, 1080p, television 1080p']['Carbon footprint'].values[0])

video_streaming_4k_carbon_footprint = video_streaming_time * video_4k/100 * (lca_data_location[lca_data_location['Name'] == 'video streaming, 4K, television 4K']['Carbon footprint'].values[0])

music_streaming_carbon_footprint = music_streaming_time * (music_smartphone/100 * lca_data_location[lca_data_location['Name'] == 'music streaming, standard quality, smartphone']['Carbon footprint'].values[0] + 
                                                   music_tablet/100 * lca_data_location[lca_data_location['Name'] == 'music streaming, standard quality, tablet']['Carbon footprint'].values[0] + 
                                                   music_laptop/100 * lca_data_location[lca_data_location['Name'] == 'music streaming, standard quality, laptop']['Carbon footprint'].values[0] + 
                                                   music_desktop/100 * lca_data_location[lca_data_location['Name'] == 'music streaming, standard quality, desktop computer']['Carbon footprint'].values[0])


conferencing_only_audio_carbon_footprint = video_conferencing_time * conferencing_only_audio/100 * (conferencing_laptop/100 * lca_data_location[lca_data_location['Name'] == 'video conferencing, audio only, laptop']['Carbon footprint'].values[0] + 
                                                                                                conferencing_desktop/100 * lca_data_location[lca_data_location['Name'] == 'video conferencing, audio only, desktop computer']['Carbon footprint'].values[0])
conferencing_audio_and_video_carbon_footprint = video_conferencing_time * conferencing_audio_and_video/100 * (conferencing_laptop/100 * lca_data_location[lca_data_location['Name'] == 'video conferencing, video standard quality, laptop']['Carbon footprint'].values[0] + 
                                                                                                conferencing_desktop/100 * lca_data_location[lca_data_location['Name'] == 'video conferencing, video standard quality, desktop computer']['Carbon footprint'].values[0])

carbon_footprint_user = {
                         'Web surfing': web_surfing_carbon_footprint,
                         'Social media': social_media_carbon_footprint,
                         'Video streaming': video_streaming_480p_carbon_footprint + video_streaming_720p_carbon_footprint + video_streaming_1080p_carbon_footprint + video_streaming_4k_carbon_footprint,
                         'Music streaming': music_streaming_carbon_footprint,
                         'Video conferencing': conferencing_only_audio_carbon_footprint + conferencing_audio_and_video_carbon_footprint,
                       }

fig_length = {1:   3.50394,    # 1 column
              1.5: 5.35433,    # 1.5 columns
              2:   7.20472}    # 2 columns
fig_height = 9.72441 # maxium height

fontsize_title = 9
fontsize_label = 8
fontsize_legend = 8
fontsize_axs = 8

spineline_width = 0.6

if display_results:
    with results:
        st.markdown("""---""")
        st.subheader('Your digital carbon footprint is:')
        st.subheader(str(round(sum(carbon_footprint_user.values()))) + ' kg CO$_2$-eq per year')

      #  c1, c2 = st.columns(2)
      #  plt.rcParams['figure.facecolor'] = 'None'
      #  fig, axs = plt.subplots(1, 1, figsize=(fig_length[1], fig_height*0.5))
      #  pd.DataFrame(carbon_footprint_user, index=['Impact']).T.plot.pie(ax=axs, y='Impact', fontsize=fontsize_axs, legend=False)

      #  c1.pyplot(fig)

       # st.bar_chart(pd.DataFrame(carbon_footprint_user, index=['Impact']))
    