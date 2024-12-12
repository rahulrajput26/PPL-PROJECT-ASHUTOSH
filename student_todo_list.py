# Import necessary libraries
import streamlit as st

# Initialize session state for tasks
if 'tasks' not in st.session_state:
    st.session_state.tasks = []  # List of active tasks
if 'done_tasks' not in st.session_state:
    st.session_state.done_tasks = []  # List of completed tasks

# Title of the app
st.title("Student To-Do List")

# Input field to add a new task
task = st.text_input("Enter a task", placeholder="e.g., Complete assignment")

# Button to add task
if st.button("Add Task"):
    if task:  # Ensure the task is not empty
        st.session_state.tasks.append(task)
        st.success(f"Task '{task}' added!")
    else:
        st.error("Task cannot be empty.")

# Display active tasks
st.subheader("Your To-Do List")
if st.session_state.tasks:
    for idx, t in enumerate(st.session_state.tasks):
        # Use a unique key for each checkbox
        if st.checkbox(f"{t}", key=f"task-{idx}"):
            # Move the task to completed
            st.session_state.done_tasks.append(t)
            st.session_state.tasks.pop(idx)
            st.experimental_rerun()
else:
    st.write("No tasks added yet!")

# Display completed tasks
st.subheader("Completed Tasks")
if st.session_state.done_tasks:
    for idx, t in enumerate(st.session_state.done_tasks):
        col1, col2 = st.columns([6, 1])
        with col1:
            st.write(f"✔ {t}")
        with col2:
            # Button to delete completed task
            if st.button("❌", key=f"done-delete-{idx}"):
                st.session_state.done_tasks.pop(idx)
                st.experimental_rerun()
else:
    st.write("No tasks completed yet!")

# Option to clear all tasks
if st.button("Clear All Tasks"):
    st.session_state.tasks.clear()
    st.session_state.done_tasks.clear()
    st.success("All tasks cleared!")