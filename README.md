# stock-information-dashboard
This is a dashboard designed to help users make informed investment decisions.

## Inspiration
When I opened my first investment account, I was head-over-heels with emotion. I couldn't wait to start buying and selling stocks of the worlds most renown companies. 

However, before I knew it, I had lost fifteen percent of my investment. Instead of blindly clicking buy and sell, I needed to make sure that my investment decisions were evidence-backed.

To solve this problem, I did what any one would do: I opened Google. I was bombarded by a list of expensive results from the worlds top financial institutions, and as I scrolled through what each of these institutions offered to their clients, I thought:

What if I could make a free application to help users make informed investment decisions that catered to the average investor, like myself?

## Description
To use the application, input a ticker symbol for any company you wish and click the submit button. On the left side, you will see financial information about the company. On the right side, you will see a sentiment analysis (VADER) of the company and recent news articles about the company. 
    
This project was built using React for the frontend and Python for the backend.

## Instructions
To run this project,

1. `git clone https://github.com/eeshangarr/TickerInsight.git`
2.  Open the cloned folder in any environment of your choice.
3.  To install packages and dependencies in `package.json`:
     -  Navigate to Terminal
     - `cd frontend/app`
     - `npm install`
4.  Now, you will need to open two separate terminals:
    - In the first terminal, `cd frontend/app` & `npm start`.
    - In the second terminal, `cd backend` & `py/python3 -m flask run`. (Hint: If you're on Windows, use `py`. If you're on MacOS, use `python3`.)
5. Go to your browser and open `localhost:3000` to view the project!

## Credits
Eeshan Garr
