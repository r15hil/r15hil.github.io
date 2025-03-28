[__Back to home__](../index.md)

<script>
    function checkWord() {
        var inputWord = document.getElementById("searchWord").value;
        var pageText = document.body.innerText;
        var wordRegex = new RegExp("\\b" + inputWord + "\\b", "gi");
        var found = pageText.match(wordRegex) !== null;
        var resultElement = document.getElementById("foundBook");
        resultElement.textContent = found ? "Yes" : "No";
    }

    function countYearOccurrences() {
        var currentYear = new Date().getFullYear();
        var pageText = document.body.innerText;
        var yearRegex = /\b(20[1-9][0-9]|21[0-9][0-9])\b/g;
        var yearOccurrences = {};

        var matches = pageText.match(yearRegex);

        if (matches) {
            matches.forEach(function(match) {
                if (yearOccurrences[match]) {
                    yearOccurrences[match]++;
                } else {
                    yearOccurrences[match] = 1;
                }
            });
        }

        var yearList = document.getElementById("yearList");
        var resultHTML = "";

        for (var year = 2016; year <= currentYear; year++) {
            var count = yearOccurrences[year.toString()] || 0;
            if (count > 0) {
                resultHTML += "<li>" + year + ": " + count + "</li>";
            }
        }

        yearList.innerHTML = resultHTML;
    }

</script>

# Books I've read

<label for="searchWord">Check if I have read:</label>
<input type="text" id="searchWord">
<button onclick="checkWord()">Check</button>
<button onclick="countYearOccurrences()">Count books</button>

<p id="foundBook"></p>

<ul id="yearList"></ul>


## Key
📚 Reading |
✅ Read |
👍 Enjoyed |
👌 Ok |
😕 Meh |
❤️ Recommend |


## Books

📚 Heaven: Mieko Kawakami

📚 Mahabharata: Interpreted and Retold by Krishna Dharma

✅ A History of Burning: Janika Oza - March 2025 👍

✅ Who Moved My Cheese?: Dr Spencer Johnson - March 2025 👌

✅ Shantaram: Gregory David Roberts - February 2025 👍❤️

✅ Men Are from Mars, Women Are from Venus: John Gray - November 2024 👌   

✅ Ultra-Processed People: Chris van Tulleken - October 2024 👍

✅ Troy: Stephen Fry - October 2024 👍

✅ Heroes: Stephen Fry - September 2024 👍❤️

✅ Four Thousand Weeks: Oliver Burkeman - August 2024 👍

✅ God Emperor of Dune: Frank Herbert - August 2024 😕

✅ Children of Dune: Frank Herbert - July 2024 👍

✅ My Experiments with Truth: M.K. Gandhi - June 2024 👍

✅ Dune Messiah: Frank Herbert - June 2024 👍

✅ The Alchemist: Paulo Coelho - June 2024 ❤️

✅ Born to Run: Christopher McDougall - May 2024 ❤️

✅ Dune: Frank Herbert - May 2024 ❤️

✅ The Psychology of Money: Morgan Housel - April 2024 👌

✅ A Wizard of Earthsea: Ursula K. Le Guin - March 2024 👍

✅ Fahrenheit 451: Ray Bradbury - February 2024 👍

✅ Surely You're Joking, Mr. Feynman!: Richard P. Feynman - December 2023 👍

✅ What Does It All Mean?: Thomas Nagel - December 2023 👍

✅ Pachinko: Min Jin Lee - November 2023 👍❤️

✅ Where the Crawdads Sing: Delia Owens - October 2023 👍

✅ Surviving to Drive: Guenther Steiner - August 2023 👍

✅ The Art of War: Sun Tzu - August 2023 👌

✅ Essentialism: Greg McKeown - August 2023 👌

✅ Kafka on the Shore: Haruki Murakami - August 2023 👍

✅ The Kite Runner: Khaled Hosseini - July 2023 👍

✅ Uncommon Wealth: Kojo Koram - June 2023 👌

✅ Flowers for Algernon: Daniel Keyes - May 2023 👍❤️

✅ Can't Hurt Me: David Goggins - May 2023 👍

✅ This is Going to Hurt: Adam Kay - April 2023 👍

✅ The Defining Decade: Why Your Twenties Matter: Meg Jay - March 2023 👌

✅ How to Win Friends and Influence People: Dale Carnegie - March 2023 👍

✅ Rebel Ideas: Matthew Syed - February 2023 👌

✅ Mythos: Stephen Fry - January 2023 👍❤️

✅ 1984: George Orwell - December 2022 👍

✅ Animal Farm: George Orwell - November 2022 👍

✅ Bhagavad Gita: Introduced & Translated by Eknath Easwaran - November 2022 👍❤️

✅ Prisoners of Geography: Tim Marshall - October 2022 👍

✅ Sapiens: Yuval Noah Harari - October 2022 👍❤️

✅ Brave New World: Aldous Huxley - October 2022 👍

✅ Tools of Titans: Tim Ferriss - March 2021 👌

✅ The Chimp Paradox: Steve Peters - February 2021 👍❤️

✅ Atomic habits: James Clear - January 2021 👌

✅ When Breath Becomes Air: Paul Kalanithi - January 2018 👍

✅ Colorless Tsukuru Tazaki and His Years of Pilgrimage: Haruki Murakami - October 2017

✅ The Humans: Matt Haig - August 2017 👌

✅ Lord of the Flies: William Golding - November 2016 👌

## Reading List

🔜 The Golden Road - William Dalrymple

🔜 I, Superorganism - Jon Turney

🔜 Guns, Germs, and Steel - Jared Diamond

🔜 Thinking, Fast and Slow - Daniel Kahneman

🔜 Why We Sleep - Matthew Walker

🔜 The ONE Thing - Gary Keller and Jay Papasan

🔜 The Beekeeper of Aleppo - Christy Lefteri

🔜 The 4-Hour Work Week - Tim Ferriss

🔜 Deep Work - Cal Newport

🔜 Heaven - Mieko Kawakami