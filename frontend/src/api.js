import axios from 'axios';

const API_BASE = 'http://localhost:8000/tasks';

export const getTasks = (params = {}) => axios.get(API_BASE, { params });
export const getTask = (taskId) => axios.get(`${API_BASE}/${taskId}`);
export const createTask = (data) => axios.post(API_BASE, data);
export const updateTask = (taskId, data) => axios.put(`${API_BASE}/${taskId}`, data);
export const deleteTask = (taskId) => axios.delete(`${API_BASE}/${taskId}`);
export const createManyTasks = (tasks) => axios.post(`${API_BASE}/group`, tasks);
export const getTasksByStatus = (status) => axios.get(`${API_BASE}/status/${status}`);
export const getTasksByPriority = (priority) => axios.get(`${API_BASE}/priority/${priority}`);
