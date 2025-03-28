import streamlit as st
import speedtest


st.set_page_config(
    page_title="How Bad Is Your Wi-Fi?",
    layout="centered"
)


st.caption("Wanna see why your videos load like they're powered by hope?")


if st.button("Test My Internet"):
    with st.spinner("Running your speed test... Please hold."):
        test = speedtest.Speedtest()
        download_speed = round(test.download() / 10**6, 2)
        upload_speed = round(test.upload() / 10**6, 2)
        ping = round(test.results.ping, 2)

    st.subheader("📊 Results")
    st.write(f"**Download Speed:** {download_speed} Mbps")
    st.write(f"**Upload Speed:** {upload_speed} Mbps")
    st.write(f"**Ping:** {ping} ms")

    
    st.subheader("Your Download Situation:")
    if download_speed < 5:
        st.error("Yo. Your internet so slow, I bet when you click 'Download', even your shadow leaves the room out of embarrassment.")
    elif download_speed < 25:
        st.warning("That’s... functional, I guess. But don’t even think about streaming anything in HD.")
    elif download_speed < 100:
        st.info("Decent. You’re surfing the net without embarrassment.")
    else:
        st.success("God DAMN it! Your connection’s flexing harder than a gym bro on pre-workout.")

    
    st.subheader("Your Upload Reality:")
    if upload_speed < 3:
        st.error("Bruh... you tryna upload with that? I’ve seen pigeons deliver data faster.")
    elif upload_speed < 10:
        st.warning("You’ll get there... eventually. Maybe upload overnight and hope it finishes before the sun explodes.")
    elif upload_speed < 100:
        st.info("Solid. You're not breaking records, but you're doing fine.")
    else:
        st.success("The GOAT. Blink and your file’s already in the cloud. Respect.")
    
    st.subheader("Your Response Time:")
    if ping > 100:
        st.error("This latency could make a sloth impatient.")
    elif ping > 50:
        st.warning("That delay you feel in Zoom? That’s your voice arriving after you do.")
    else:
        st.success("Smooth sailing. Your reactions actually show up in real time.")


else:
    st.info("Click the button above when you're brave enough to face the truth 😤")
