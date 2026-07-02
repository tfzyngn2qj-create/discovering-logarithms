import streamlit as st
import math

st.set_page_config(page_title="Discovering Logarithms", page_icon="🧩")

st.title("Discovering Logarithms")
st.subheader("The Missing Exponent Puzzle by Mac Murray")

if "step" not in st.session_state:
    st.session_state.step = 0

if "answered" not in st.session_state:
    st.session_state.answered = False


def next_step():
    st.session_state.step += 1
    st.session_state.answered = False
    st.rerun()


problems = [
    {
        "type": "question",
        "prompt": r"2^3 = ?",
        "answer": "8",
        "success_text": "Yes! $2^3 = 8$ because $2 \\times 2 \\times 2 = 8$. That means 2 is multiplied by itself 3 times.",
        "hint": "Try multiplying 2 three times.",
    },
    {
        "type": "question",
        "prompt": r"5^2 = ?",
        "answer": "25",
        "success_text": "Exactly! $5^2 = 25$ because $5 \\times 5 = 25$. That means 5 is multiplied by itself 2 times.",
        "hint": "Try multiplying 5 two times.",
    },
    {
        "type": "question",
        "prompt": r"10^3 = ?",
        "answer": "1000",
        "success_text": "Right! $10^3 = 1000$ because $10 \\times 10 \\times 10 = 1000$.",
        "hint": "Think of 10 times 10 times 10.",
    },
    {
        "type": "question",
        "prompt": r"16^{1/2} = ?",
        "answer": "4",
        "success_text": "Yes! Remember the root rule: raising something to the $1/n$ power means taking the $n$th root. In this case $n=2$, so $16^{1/2}=\\sqrt{16}=4$.",
        "hint": "A power of $1/2$ means square root.",
    },
    {"type": "mystery"},
    {
        "type": "transform",
        "title": "Now watch the exponent equation transform.",
        "exp": r"2^3 = 8",
        "log": r"\log_2(8)=3",
        "explanation": "The base stays 2. The answer, 8, moves inside the logarithm. The exponent, 3, becomes the answer.",
    },
    {
        "type": "transform",
        "title": "Another one.",
        "exp": r"5^2 = 25",
        "log": r"\log_5(25)=2",
        "explanation": "Again: the logarithm asks for the missing exponent.",
    },
    {
        "type": "transform",
        "title": "One more.",
        "exp": r"10^3 = 1000",
        "log": r"\log_{10}(1000)=3",
        "explanation": "This says: 10 raised to what power gives 1000?",
    },
    {
        "type": "try",
        "prompt": r"3^4 = 81",
        "correct_base": "3",
        "correct_argument": "81",
        "correct_result": "4",
        "success_text": "Yes! $3^4 = 81$ transforms into $\\log_3(81)=4$.",
        "hint": "Use the pattern: base stays the base, answer goes inside the log, exponent becomes the answer.",
    },
    {
        "type": "try",
        "prompt": r"4^2 = 16",
        "correct_base": "4",
        "correct_argument": "16",
        "correct_result": "2",
        "success_text": "Exactly! $4^2 = 16$ transforms into $\\log_4(16)=2$.",
        "hint": "Base = 4, argument = 16, answer = 2.",
    },
    {
        "type": "try",
        "prompt": r"9^{1/2} = 3",
        "correct_base": "9",
        "correct_argument": "3",
        "correct_result": "1/2",
        "success_text": "Nice! $9^{1/2}=3$ transforms into $\\log_9(3)=1/2$.",
        "hint": "Base = 9, argument = 3, answer = 1/2.",
    },
    {"type": "discovery"},
    {"type": "revisit"},
    {"type": "useful"},
]

step = st.session_state.step
current = problems[step]

st.progress((step + 1) / len(problems))


if current["type"] == "question":
    st.markdown("### Solve the exponent puzzle:")
    st.latex(current["prompt"])

    answer = st.text_input("Your answer", key=f"answer_{step}")

    if st.button("Check"):
        if answer.strip() == current["answer"]:
            st.session_state.answered = True
            st.success("Correct!")
        else:
            st.warning(current["hint"])

    if st.session_state.answered:
        st.markdown(current["success_text"])
        st.button("Next", on_click=next_step)


elif current["type"] == "mystery":
    st.markdown("## But what if the exponent is missing?")

    st.markdown("So far, these had nice answers:")
    st.latex(r"2^3=8")
    st.latex(r"5^2=25")
    st.latex(r"10^3=1000")
    st.latex(r"16^{1/2}=4")

    st.markdown("But what would you say if someone asked you this?")

    st.latex(r"2^?=20")

    st.markdown(
        """
That is harder because 20 is not a clean power of 2.

We know:
"""
    )

    st.latex(r"2^4=16")
    st.latex(r"2^5=32")

    st.markdown(
        """
So the missing exponent is not 4 and it is not 5.

It must be somewhere between 4 and 5.

Instead of guessing forever, mathematicians gave this missing exponent a name.
"""
    )

    st.button("Learn the name", on_click=next_step)


elif current["type"] == "transform":
    st.markdown(f"### {current['title']}")

    st.markdown("We already know:")
    st.latex(current["exp"])

    if st.button("Transform it"):
        st.session_state.answered = True

    if st.session_state.answered:
        st.markdown("This can be rewritten as:")
        st.latex(current["log"])
        st.info(current["explanation"])
        st.button("Next", on_click=next_step)


elif current["type"] == "try":
    st.markdown("### Your turn.")

    st.markdown("Use these examples as a reference:")

    st.latex(r"2^3 = 8 \quad \Longleftrightarrow \quad \log_2(8)=3")
    st.latex(r"5^2 = 25 \quad \Longleftrightarrow \quad \log_5(25)=2")
    st.latex(r"10^3 = 1000 \quad \Longleftrightarrow \quad \log_{10}(1000)=3")

    st.markdown("Rewrite this exponent equation as a logarithm:")
    st.latex(current["prompt"])

    st.markdown("Fill in the logarithm:")

    col1, col2, col3, col4, col5, col6 = st.columns([0.8, 0.9, 0.25, 1.1, 0.3, 0.9])

    with col1:
        st.markdown("### log")
    with col2:
        base = st.text_input("base", key=f"base_{step}", placeholder="base")
    with col3:
        st.markdown("### (")
    with col4:
        argument = st.text_input("argument", key=f"argument_{step}", placeholder="argument")
    with col5:
        st.markdown("### ) =")
    with col6:
        result = st.text_input("answer", key=f"result_{step}", placeholder="answer")

    if st.button("Check"):
        if (
            base.strip() == current["correct_base"]
            and argument.strip() == current["correct_argument"]
            and result.strip() == current["correct_result"]
        ):
            st.session_state.answered = True
            st.success("Correct!")
        else:
            st.warning(current["hint"])

    if st.session_state.answered:
        st.markdown(current["success_text"])
        st.button("Next", on_click=next_step)


elif current["type"] == "discovery":
    st.markdown("## Wow — you just discovered logarithms.")

    st.markdown(
        """
You did not start by memorizing a formula.

You started with exponent puzzles. Then you noticed that the same relationship can be written in a new way.

A logarithm is just the answer to a missing-exponent question.
"""
    )

    st.latex(r"\log_b(a)=x")
    st.markdown("means:")
    st.latex(r"b^x=a")

    st.success("So logarithms and exponents are two ways of saying the same relationship.")

    st.button("Revisit the mystery", on_click=next_step)


elif current["type"] == "revisit":
    st.markdown("## Now let’s revisit the hard question.")

    st.markdown("Earlier, this was hard to answer:")

    st.latex(r"2^?=20")

    st.markdown("Now you have a way to name that missing exponent.")

    st.markdown("Fill in the logarithm:")

    col1, col2, col3, col4, col5 = st.columns([0.8, 0.9, 0.25, 1.1, 0.3])

    with col1:
        st.markdown("### log")
    with col2:
        base = st.text_input("base", key="revisit_base", placeholder="base")
    with col3:
        st.markdown("### (")
    with col4:
        argument = st.text_input("argument", key="revisit_argument", placeholder="argument")
    with col5:
        st.markdown("### ) = ?")

    if st.button("Check"):
        if base.strip() == "2" and argument.strip() == "20":
            st.session_state.answered = True
            st.success("Yes!")
        else:
            st.warning("The base is 2 and the number we are trying to reach is 20.")

    if st.session_state.answered:
        st.markdown("The missing exponent is:")
        st.latex(r"\log_2(20)")
        st.info(f"In decimal form, this is about {math.log(20, 2):.3f}.")
        st.markdown("So:")
        st.latex(r"2^{\log_2(20)}=20")
        st.button("Next", on_click=next_step)


elif current["type"] == "useful":
    st.markdown("## Why are logarithms useful?")

    st.markdown(
        """
Logarithms are useful because many exponent questions do not have clean whole-number answers.

For example:
"""
    )

    st.latex(r"2^?=20")

    st.markdown("The answer is not 4, because:")
    st.latex(r"2^4=16")

    st.markdown("And it is not 5, because:")
    st.latex(r"2^5=32")

    st.markdown(
        """
So the missing exponent is somewhere between 4 and 5.

That is exactly what this means:
"""
    )

    st.latex(r"\log_2(20)")

    st.info(f"$\\log_2(20) \\approx {math.log(20, 2):.3f}$")

    st.markdown(
        """
This matters in real life because logarithms help us solve questions about growth, shrinking, scale, and time.

They show up in things like:

- sound levels
- earthquakes
- computer science
- population growth
- interest rates
- data science
- scientific measurements
"""
    )

    st.success("Final big idea: logarithms answer the question, “What exponent do we need?”")