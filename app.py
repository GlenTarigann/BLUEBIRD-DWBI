import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


# =========================
# CONFIG
# =========================

st.set_page_config(
    page_title="Bluebird DWBI",
    layout="wide"
)


# =========================
# PATH
# =========================

BASE_DIR = Path(__file__).resolve().parent

DATA_PATH = BASE_DIR / "data" / "bluebird_dwbi_dataset.csv"
DEMAND_PATH = BASE_DIR / "result" / "demand_analysis_results.csv"
PREDICTION_PATH = BASE_DIR / "result" / "prediction_recommendation_results.csv"


# =========================
# LOAD DATA
# =========================

@st.cache_data
def load_data():

    df = pd.read_csv(DATA_PATH)
    demand = pd.read_csv(DEMAND_PATH)
    prediction = pd.read_csv(PREDICTION_PATH)

    df["date"] = pd.to_datetime(df["date"])

    return df, demand, prediction


df, demand, prediction = load_data()

df_completed = df[
    df["status"] == "Completed"
].copy()


# =========================
# TITLE
# =========================

st.title("Bluebird Business Analytics")


# =========================
# SIDEBAR FILTER
# =========================

st.sidebar.header("Filter")

cities = sorted(
    df_completed["city"].dropna().unique()
)

selected_cities = st.sidebar.multiselect(
    "Kota",
    cities,
    default=cities
)

services = sorted(
    df_completed["service"].dropna().unique()
)

selected_services = st.sidebar.multiselect(
    "Service",
    services,
    default=services
)

filtered = df_completed[
    (df_completed["city"].isin(selected_cities)) &
    (df_completed["service"].isin(selected_services))
].copy()


if filtered.empty:

    st.warning("Tidak ada data.")

    st.stop()


# =========================
# KPI
# =========================

total_trip = len(filtered)

total_revenue = filtered["fare"].sum()

average_fare = filtered["fare"].mean()

average_rating = filtered["rating"].mean()


col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Trip",
    f"{total_trip:,}"
)

col2.metric(
    "Revenue",
    f"Rp {total_revenue:,.0f}"
)

col3.metric(
    "Average Fare",
    f"Rp {average_fare:,.0f}"
)

col4.metric(
    "Average Rating",
    f"{average_rating:.2f}"
)


# =========================
# DESCRIPTIVE
# =========================

st.header("Descriptive Analytics")


col1, col2 = st.columns(2)


with col1:

    st.subheader("Trip by City")

    trip_city = (
        filtered
        .groupby("city")["trip_id"]
        .count()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(8, 4))

    trip_city.plot(
        kind="bar",
        ax=ax
    )

    ax.set_xlabel("")
    ax.set_ylabel("Trips")
    ax.tick_params(axis="x", rotation=0)

    st.pyplot(fig)

    plt.close(fig)


with col2:

    st.subheader("Trip by Hour")

    trip_hour = (
        filtered
        .groupby("hour")["trip_id"]
        .count()
    )

    fig, ax = plt.subplots(figsize=(8, 4))

    trip_hour.plot(
        kind="line",
        marker="o",
        ax=ax
    )

    ax.set_xlabel("Hour")
    ax.set_ylabel("Trips")

    st.pyplot(fig)

    plt.close(fig)


st.subheader("Trip by Service")

trip_service = (
    filtered
    .groupby("service")["trip_id"]
    .count()
    .sort_values(ascending=False)
)

fig, ax = plt.subplots(figsize=(10, 4))

trip_service.plot(
    kind="bar",
    ax=ax
)

ax.set_xlabel("")
ax.set_ylabel("Trips")
ax.tick_params(axis="x", rotation=0)

st.pyplot(fig)

plt.close(fig)


# =========================
# DIAGNOSTIC
# =========================

st.header("Diagnostic Analytics")


st.subheader("Demand by City and Hour")

city_hour = pd.pivot_table(
    filtered,
    values="trip_id",
    index="city",
    columns="hour",
    aggfunc="count",
    fill_value=0
)

fig, ax = plt.subplots(
    figsize=(14, 5)
)

sns.heatmap(
    city_hour,
    cmap="Blues",
    ax=ax
)

ax.set_xlabel("Hour")
ax.set_ylabel("City")

st.pyplot(fig)

plt.close(fig)


st.subheader("Correlation")

correlation_columns = [
    "fare",
    "distance_km",
    "duration_minute",
    "rating",
    "available_fleet"
]

correlation = filtered[
    correlation_columns
].corr()

fig, ax = plt.subplots(
    figsize=(8, 5)
)

sns.heatmap(
    correlation,
    annot=True,
    fmt=".2f",
    cmap="Blues",
    ax=ax
)

st.pyplot(fig)

plt.close(fig)


# =========================
# PREDICTIVE
# =========================

st.header("Predictive Analytics")


if "predicted_demand" in prediction.columns:

    if "city" in prediction.columns:

        predicted_city = (
            prediction
            .groupby("city")["predicted_demand"]
            .mean()
            .sort_values(ascending=False)
        )

        st.subheader("Predicted Demand by City")

        fig, ax = plt.subplots(
            figsize=(10, 4)
        )

        predicted_city.plot(
            kind="bar",
            ax=ax
        )

        ax.set_xlabel("")
        ax.set_ylabel("Predicted Demand")
        ax.tick_params(axis="x", rotation=0)

        st.pyplot(fig)

        plt.close(fig)


st.subheader("Prediction Results")

st.dataframe(
    prediction,
    use_container_width=True
)


# =========================
# PRESCRIPTIVE
# =========================

st.header("Prescriptive Analytics")


if "recommendation" in prediction.columns:

    recommendation_count = (
        prediction["recommendation"]
        .value_counts()
    )

    col1, col2 = st.columns([1, 2])


    with col1:

        st.subheader("Recommendation")

        fig, ax = plt.subplots(
            figsize=(6, 4)
        )

        recommendation_count.plot(
            kind="bar",
            ax=ax
        )

        ax.set_xlabel("")
        ax.set_ylabel("Count")
        ax.tick_params(axis="x", rotation=20)

        st.pyplot(fig)

        plt.close(fig)


    with col2:

        st.subheader("Recommendation Results")

        st.dataframe(
            prediction,
            use_container_width=True
        )


# =========================
# DATA
# =========================

st.header("Data")

st.dataframe(
    filtered,
    use_container_width=True
)

