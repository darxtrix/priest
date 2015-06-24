![](http://assets.flatcartoon.com/images/3.png)

#priest

Generate wishes from your command line with full customization.

**Clueless ?**

# Okay, see this
- If you try this in **night** :

```bash
>>> from priest import now
>>> now()
    #=> good night, have sweet dreams !!
    #=> howdy, nighttime :-)
```

- If you try this in **morning** :

```bash
>>> from priest import now
>>> now()
    #=> hey, morning !
    #=> heya !! morning !
```
        
**PS:** You can run this at any time of a day , it will generate wish messages accordingly. :smiley:

# See more
- If you run it in **France** in night
    
```bash
>>> from priest import now
>>> now()
    # = > Bonne nuit , beaux rêves !!
```

- If you run it in **Germany** in night

```bash
>>> from priest import now
>>> now()
    # => Gute Nacht, süße Träume haben !!
```
        

# Not impressed ?
And, this gives you an awesome picture message :wink:

```bash
>>> from priest import now
>>> now(lang='en',pic=True)
```
    
![](http://i.imgur.com/pG2FRcr.jpg)

# What is does and how ?
It generates random wish messages/pictures in your native language and according to time of the day by querying APIs internally for getting the information of your timezone, location etc.
**Note** : If you are using a proxy connection, it might create a mess ! :flushed:

# Usage
###methods
`now` -  Generates a wish according to current time of the day    
`morning` -  Outputs a morning greeting message   
`afternoon` -  Outputs a afternoon greeting message   
`evening` -  Outputs a evening greeting message  
`night`-  Outputs a night greeting message   

##parameters 
Each method takes in a `lang` parameter for eg. `en`,`de` etc and you can pass in an optional `pic` parameter.

```bash
>>> from priest import morning
>>> morning(lang='de',pic=True)
```

![](http://i.imgur.com/hv8URIf.jpg)


#Installing

```bash
>>> pip install priest
```

**Note** : You need to register at [Mashape](https://www.mashape.com) and set your api key as an environment variable. i.e

```bash
>>> export X_Mashape_Key=<api-key>
```
    
# Some feature storming
- Rest API coming soon !
- Use calendar API to generate wishes for festivals.

# Contributions
Pull requests are awesome and always welcome. Please use the **issue tracker** to report any bugs or file feature requests.

#Licence 
MIT


