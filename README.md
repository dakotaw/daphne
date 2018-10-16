# daphne

Helper tool for snagging those nifty Reply All Freddie toys. 

## Background

In 2015, Mailchimp ran a promotional campaign with Gimlet's [Reply All podcast](https://www.gimletmedia.com/reply-all/all). Every few weeks, the podcast hosts would announce that a new Freddie toy was available for the first people to navigate to a promo website and request one. This was my favorite podcast at the time, and I have always loved the Mailchimp brand, so I was very invested in getting the Freddie toys. Unfortunately, they were almost always gone by the time I got around to listening to the podcast. 

This tool periodically pings the website where new Freddie toys are announced. It performs an extremely rudimentary parsing of the HTML, determines the name of the Freddie toy, and compares it to the toy that was last posted on the website. When there's a change, it will email the designated address. It's simple, but I was able to snag about 10 of the Freddie toys with its help! 
