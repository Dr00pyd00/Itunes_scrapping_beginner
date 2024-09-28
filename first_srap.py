import requests
import json

def main():

    #documentation:
    '''It's a programm who scrapt some data of network ,
     by artitst and try  copy the data organized in a text document!'''


   #ask to user a name artist and a number of song he wanna see:
    artist_user = input("Which artist or song? ").title()
    num_data = int(input("How many songs ? "))

    #resquests with url api itunes with users inputs:
    user_data = f'https://itunes.apple.com/search?entity=song&term={artist_user}&limit={num_data}'

    #i use function for requests data and  transform data into json:
    user_itunes_data = get_data_online(user_data)


#MY LISTS:

    #create list of names :

    '''here i training to do comprehension list with names:
      artist_name_list  = [  ]
    for index in range(num_data):
        artist_name_list.append(user_itunes_data['results'][index]['artistName'])
    '''

    art_name_list = [user_itunes_data['results'][index]['artistName'] for index in range(num_data) ]

    #test my list:
    # print(art_name_list)

    #create list of songs names :

    song_name_list = [ user_itunes_data['results'][index]['trackName'] for index in range(num_data)]


    #create list of date of the song : [0:9] for clearify data date !

    date_song_list = [ user_itunes_data['results'][index]['releaseDate'][0:10] for index in range(num_data)]
    # print(date_song_list)


    #create a list zip with my 3 lists:
    full_values_list = zip(art_name_list, song_name_list, date_song_list)

    ##test:
    # print('lsit colmplete avec tuple:')
    # print(list(full_values_list))
    # print()

    #prepare my test line :

    #again my zip list because print() EXAUST AND del the conain of my list :( :
    full_values_list = zip(art_name_list, song_name_list, date_song_list)

    text_list = []

    #check if sorted by itune was wrong and confond name artist with name of song , so i delete the issues:

    for name, song, date in full_values_list:
        if name == artist_user:
            text = f' *** The artist is {name} // Song name: {song}  // date: {date}'
            text_list.append(text)
        else:
            pass
    #test de text_list:
    # print('List of texts:')
    # print(text_list)



    #write line by line the text in the document text:


    with open('itunes_scrap.txt', 'a') as file:
        # print('file open sucess')
        for line in text_list:
            # print(f'the line is {line}')
            file.write(line + '\n')
            file.write('\n')




#jsut a funct who gonna take data of the internet:
def get_data_online(url):

    #get data:
    requests.get(url)
    #transform in json():
    itu_data = (requests.get(url)).json()

    '''i can vizualize better for human using :
    print(json.dumps(itu_data, indent=1)) '''

    return itu_data


if __name__ =='__main__':
    main()
