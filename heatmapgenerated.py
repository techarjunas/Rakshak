
import geopandas
from firebase import firebase

df = geopandas.read_file("H:/techarjunas/firebase/indianstates/Indian_States.shp")
firebase1 = firebase.FirebaseApplication("https://rakshaksih.firebaseio.com/", None)


# In[47]:

print(df)


# In[41]:

def generate_heat_map() :
    
    data = firebase1.get('state','')
    registered_users =[]
    for i in data:
        # for y in data[i] :
        z = (float(data[i]['casescount'])/float(data[i]['population'])*10000,data[i]['statename'])
        registered_users.append(z)
    print(registered_users)
    state_corona = (registered_users)


    # In[46]:


    # state_corona


    # In[2]:


    # state_corona = [('4000', 'Jammu and Kashmir'), ('11000', 'Karnataka'), ('19000', 'NCR of Delhi'), ('200', 'Puducherry '), ('8000', 'Andhra Pradesh'), ('5000', 'Daman and Diu'), ('5000', 'Rajasthan'), ('25000', 'Maharashtra'), ('8000', 'Bihar'), ('6000', 'Odisha'), ('3000', 'Mizoram '), ('30000', 'Assam'), ('15000', 'Madhya Pradesh'), ('1000', 'Manipur'), ('10500', 'Himachal Pradesh'), ('4500', 'Ladakh'), ('50000', 'Tamil Nadu'), ('25000', 'Chattisgarh'), ('9000', 'Jharkhand'), ('1000', 'Chandigarh'), ('400', 'Goa'), ('11500', 'Punjab'), ('500', 'Meghalaya'), ('6000', 'Dadar and Nagar Haveli'), ('4500', 'Lakshwadeep'), ('2000', 'Arunachal Pradesh'), ('7000', 'Nagaland'), ('9000', 'Kerala'), ('7000', 'Haryana')]


    # In[43]:


    df['hue'] = 0.00000
    df.at[24,'st_nm'] = "Delhi"
    for j in range(len(df)):
        df.at[j,'st_nm'] = df.at[j,'st_nm'].lower()


    # In[44]:


    for i in state_corona:
        d = df[df['st_nm']==i[1].lower()].index.values.astype(int)
        df.at[d,'hue'] = int(i[0])


    # In[45]:


    a = df.plot(column='hue',cmap='OrRd',k=None,legend=True,edgecolor='black',figsize=(8, 10))


    # In[37]:


    fig = a.get_figure()


    # In[38]:


    # fig


    # In[8]:


    fig.savefig("myplot.png")

# generate_heat_map()