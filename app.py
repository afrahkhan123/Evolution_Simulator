import streamlit as st
import matplotlib.pyplot as plt

from simulation import run_simulation


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Evolution Simulator",
    page_icon="🧬",
    layout="wide"
)


# =========================================================
# CUSTOM STYLING
# =========================================================

st.markdown("""
<style>
.stApp {
    background-color: #0F172A;
}

.block-container {
    max-width: 1500px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

h1, h2, h3, h4 {
    color: #F8FAFC !important;
}

p, label {
    color: #E2E8F0;
}

hr {
    border-color: #334155;
    margin: 12px 0;
}

.stButton > button {
    background-color: #172033;
    color: #F8FAFC;
    border: 1px solid #334155;
    border-radius: 12px;
    min-height: 58px;
    padding: 8px;
    font-size: 14px;
    font-weight: 600;
}

.stButton > button:hover {
    background-color: #1E293B;
    border-color: #38BDF8;
    color: #E0F2FE;
}

.stCaption {
    color: #7F9BBC !important;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    border-color: #334155;
    border-radius: 14px;
    background-color: #111F38;
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div style="text-align:center; padding:8px 0 18px 0;">
    <div style="font-size:50px;">🧬</div>
    <h1 style="font-size:42px; margin:0;">Evolution Simulator</h1>
    <p style="color:#94D2FF !important; font-size:19px; margin:8px 0 2px 0;">
        Explore how species adapt under natural pressures.
    </p>
    <p style="color:#64748B !important; font-size:13px; margin:0;">
        A visual simulation of natural selection driven by environmental change.
    </p>
</div>
""", unsafe_allow_html=True)


# =========================================================
# SPECIES SELECTOR
# =========================================================

species = [
    "🦟 Mosquito — Insecticide Resistance",
    "🍀 White Clover — Urban Evolution",
    "🦎 Anole Lizard — City Adaptation",
    "🦋 Peppered Moth — Industrial Melanism"
]

if "selected_species" not in st.session_state:
    st.session_state.selected_species = species[0]

species_cols = st.columns(4)

for i, name in enumerate(species):
    short_name = name.split(" — ")[0]

    with species_cols[i]:
        if st.button(short_name, key=f"species_{i}", use_container_width=True):
            st.session_state.selected_species = name

selected_species = st.session_state.selected_species

st.markdown(
    f"**Selected:** {selected_species}"
)

st.divider()


# =========================================================
# MAIN DASHBOARD
# =========================================================

controls, graphs = st.columns([0.8, 1.6], gap="large")


# =========================================================
# CONTROLS
# =========================================================

with controls:

    st.header("Configure Environment")
    st.caption("Adjust environmental pressures and observe the response.")

    # -----------------------------------------------------
    # MOSQUITO
    # -----------------------------------------------------

    if "Mosquito" in selected_species:

        st.subheader("Environmental Conditions")

        pesticide = st.slider("Insecticide Exposure", 0, 100, 50)
        st.caption("Intensity of insecticide affecting mosquito survival.")

        temperature = st.slider("Temperature", 0, 100, 50)
        st.caption("Environmental temperature affecting population fitness.")

        st.subheader("Additional Conditions")

        food = st.slider("Food Availability", 0, 100, 50)
        st.caption("Availability of resources supporting population growth.")

        urbanization = st.slider("Urbanization", 0, 100, 20)
        st.caption("Degree of urban environmental pressure.")

        generations, population, trait_frequency, fitness = run_simulation(
            species=selected_species,
            pesticide=pesticide,
            temperature=temperature,
            food=food,
            urbanization=urbanization
        )

        trait_name = "Insecticide Resistance"
        species_emoji = "🦟"


    # -----------------------------------------------------
    # WHITE CLOVER
    # -----------------------------------------------------

    elif "White Clover" in selected_species:

        st.subheader("Environmental Conditions")

        temperature = st.slider(
            "Winter Temperature / Frost Pressure", 0, 100, 50
        )
        st.caption("Relative cold and frost pressure affecting cyanogenesis.")

        herbivory = st.slider("Herbivore Pressure", 0, 100, 50)
        st.caption("Pressure from herbivores that cyanogenesis can deter.")

        st.subheader("Additional Conditions")

        moisture = st.slider("Moisture Availability", 0, 100, 50)
        st.caption("Environmental moisture supporting population growth.")

        urbanization = st.slider("Urbanization", 0, 100, 20)
        st.caption("Urban-rural environmental gradient.")

        generations, population, trait_frequency, fitness = run_simulation(
            species=selected_species,
            temperature=temperature,
            herbivory=herbivory,
            moisture=moisture,
            urbanization=urbanization
        )

        trait_name = "Cyanogenesis"
        species_emoji = "🍀"


    # -----------------------------------------------------
    # ANOLE
    # -----------------------------------------------------

    elif "Anole Lizard" in selected_species:

        st.subheader("Environmental Conditions")

        urbanization = st.slider("Urbanization", 0, 100, 50)
        st.caption("Degree of urban habitat and artificial surfaces.")

        surface_smoothness = st.slider("Surface Smoothness", 0, 100, 50)
        st.caption("Availability of smooth surfaces requiring adhesion.")

        st.subheader("Additional Conditions")

        temperature = st.slider("Temperature", 0, 100, 50)
        st.caption("Environmental temperature affecting population fitness.")

        humidity = st.slider("Humidity", 0, 100, 50)
        st.caption("Environmental humidity affecting population conditions.")

        generations, population, trait_frequency, fitness = run_simulation(
            species=selected_species,
            urbanization=urbanization,
            surface_smoothness=surface_smoothness,
            temperature=temperature,
            humidity=humidity
        )

        trait_name = "Urban Toepad Adaptation"
        species_emoji = "🦎"


    # -----------------------------------------------------
    # PEPPERED MOTH
    # -----------------------------------------------------

    else:

        st.subheader("Environmental Conditions")

        pollution = st.slider(
            "Pollution / Background Darkening", 0, 100, 50
        )
        st.caption("Environmental darkening affecting moth camouflage.")

        predator_pressure = st.slider("Predator Pressure", 0, 100, 50)
        st.caption("Strength of bird predation affecting survival and selection.")

        st.subheader("Additional Conditions")

        habitat_darkness = st.slider("Habitat Darkness", 0, 100, 50)
        st.caption("Darkness of resting surfaces available to moths.")

        food = st.slider("Food Availability", 0, 100, 50)
        st.caption("Availability of resources supporting population growth.")

        generations, population, trait_frequency, fitness = run_simulation(
            species=selected_species,
            pollution=pollution,
            predator_pressure=predator_pressure,
            habitat_darkness=habitat_darkness,
            food=food
        )

        trait_name = "Melanic Coloration"
        species_emoji = "🦋"


# =========================================================
# LIVE GRAPHS
# =========================================================

with graphs:

    st.header("Live Simulation")
    st.caption("Adjust the environment to see the evolutionary response.")

    st.subheader("Population Over Generations")

    fig, ax = plt.subplots(figsize=(8, 2.45))

    fig.patch.set_facecolor("#0F172A")
    ax.set_facecolor("#0F172A")

    ax.plot(generations, population, linewidth=2.5)

    ax.set_xlabel("Generation", color="white")
    ax.set_ylabel("Population", color="white")
    ax.tick_params(axis="both", colors="white")
    ax.grid(alpha=0.18)

    for spine in ax.spines.values():
        spine.set_color("#475569")

    fig.tight_layout()
    st.pyplot(fig,width="stretch")
    plt.close(fig)

    st.subheader(f"Evolution of {trait_name}")

    fig2, ax2 = plt.subplots(figsize=(8, 2.45))

    fig2.patch.set_facecolor("#0F172A")
    ax2.set_facecolor("#0F172A")

    ax2.plot(generations, trait_frequency, linewidth=2.5)

    ax2.set_xlabel("Generation", color="white")
    ax2.set_ylabel("Trait Frequency", color="white")
    ax2.set_ylim(0, 1)
    ax2.tick_params(axis="both", colors="white")
    ax2.grid(alpha=0.18)

    for spine in ax2.spines.values():
        spine.set_color("#475569")

    fig2.tight_layout()
    st.pyplot(fig2,width="stretch")
    plt.close(fig2)


# =========================================================
# SPECIES PROFILE
# =========================================================

st.divider()
st.header("Species Profile")

initial_trait = float(trait_frequency[0])
final_trait = float(trait_frequency[-1])
change = (final_trait - initial_trait) * 100

profile_left, profile_right = st.columns(2, gap="large")


# =========================================================
# SPECIES VISUAL / PROFILE
# =========================================================

with profile_left:

    with st.container(border=True):

        if "Mosquito" in selected_species:
            image_path = "assets/mosquito.png"

        elif "White Clover" in selected_species:
            image_path = "assets/white_clover.png"

        elif "Anole Lizard" in selected_species:
            if final_trait >= 0.5:
                image_path = "assets/anole_long_limb.png"
            else:
                image_path = "assets/anole_short_limb.png"

        else:
            if final_trait >= 0.5:
                image_path = "assets/moth_dark.png"
            else:
                image_path = "assets/moth_light.png"

        st.image(image_path, width="stretch")

        st.subheader(selected_species.split(" — ")[0])
        st.caption(trait_name)

        st.divider()

        metric1, metric2 = st.columns(2)

        with metric1:
            st.metric("Initial Trait", f"{initial_trait:.0%}")

        with metric2:
            st.metric("Final Trait", f"{final_trait:.0%}")

        st.metric("Change", f"{change:+.1f} percentage points")

        st.caption("Organism visual placeholder — future 3D render goes here.")


# =========================================================
# EVOLUTIONARY INTERPRETATION / LLM PLACEHOLDER
# =========================================================

with profile_right:

    with st.container(border=True):

        st.subheader("🧠 Evolutionary Interpretation")

        if change > 2:
            st.success("↑ Trait Increasing")
            st.write(
                "The selected trait became more common over generations."
            )

        elif change < -2:
            st.warning("↓ Trait Decreasing")
            st.write(
                "The selected trait became less common over generations."
            )

        else:
            st.info("→ Trait Relatively Stable")
            st.write(
                "The selected trait remained relatively stable over generations."
            )

        st.divider()

        st.markdown("**Simulated outcome**")
        st.markdown(f"### {initial_trait:.0%} → {final_trait:.0%}")

        st.info(
            "AI-generated biological interpretation will appear here. "
            "It will explain how the environmental conditions influenced "
            "population dynamics and trait frequency."
        )