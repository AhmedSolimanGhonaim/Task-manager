import React, { useEffect, useState } from 'react';
import { Container, Typography, Box, Button, TextField, Select, MenuItem, Paper, List, ListItem, ListItemText, AppBar, Toolbar, Stack, Dialog } from '@mui/material';
import AddTaskIcon from '@mui/icons-material/AddTask';
import TaskDetails from './TaskDetails';
import TaskGroup from './TaskGroup';
import * as api from './api';

function App() {
  const [tasks, setTasks] = useState([]);
  const [title, setTitle] = useState('');
  const [priority, setPriority] = useState('medium');
  const [loading, setLoading] = useState(false);
  const [selectedTask, setSelectedTask] = useState(null);
  const [filterStatus, setFilterStatus] = useState('');
  const [filterPriority, setFilterPriority] = useState('');
  const [groupOpen, setGroupOpen] = useState(false);

  const fetchTasks = async () => {
    setLoading(true);
    try {
      let res;
      if (filterStatus) {
        res = await api.getTasksByStatus(filterStatus);
      } else if (filterPriority) {
        res = await api.getTasksByPriority(filterPriority);
      } else {
        res = await api.getTasks();
      }
      setTasks(res.data);
    } catch {
      setTasks([]);
    }
    setLoading(false);
  };

  useEffect(() => {
    fetchTasks();
    // eslint-disable-next-line
  }, [filterStatus, filterPriority]);

  const handleAddTask = async (e) => {
    e.preventDefault();
    if (!title) return;
    try {
      await api.createTask({ title, priority });
      setTitle('');
      setPriority('medium');
      fetchTasks();
    } catch {}
  };

  const handleTaskClick = (task) => setSelectedTask(task.id);
  const handleTaskUpdated = () => { setSelectedTask(null); fetchTasks(); };
  const handleTaskDeleted = () => { setSelectedTask(null); fetchTasks(); };
  const handleClearFilters = () => { setFilterStatus(''); setFilterPriority(''); };

  return (
    <Box sx={{ bgcolor: '#f5f7fa', minHeight: '100vh' }}>
      <AppBar position="static" color="primary">
        <Toolbar>
          <AddTaskIcon sx={{ mr: 1 }} />
          <Typography variant="h6" component="div">Tasker</Typography>
        </Toolbar>
      </AppBar>
      <Container maxWidth="sm" sx={{ mt: 4 }}>
        <Paper elevation={3} sx={{ p: 3 }}>
          <Typography variant="h5" gutterBottom align="center">Create a Task</Typography>
          <Box component="form" onSubmit={handleAddTask} sx={{ display: 'flex', gap: 2, mb: 3 }}>
            <TextField
              label="Title"
              value={title}
              onChange={e => setTitle(e.target.value)}
              fullWidth
              required
            />
            <Select
              value={priority}
              onChange={e => setPriority(e.target.value)}
              required
              sx={{ minWidth: 120 }}
            >
              <MenuItem value="low">Low</MenuItem>
              <MenuItem value="medium">Medium</MenuItem>
              <MenuItem value="high">High</MenuItem>
            </Select>
            <Button type="submit" variant="contained" color="primary">Add</Button>
          </Box>
          <Button variant="outlined" sx={{ mb: 2 }} onClick={()=>setGroupOpen(true)}>Create Multiple Tasks</Button>
          <Stack direction="row" spacing={2} sx={{ mb: 2 }}>
            <Select
              value={filterStatus}
              displayEmpty
              onChange={e => { setFilterStatus(e.target.value); setFilterPriority(''); }}
              sx={{ minWidth: 140 }}
            >
              <MenuItem value="">Filter by Status</MenuItem>
              <MenuItem value="pending">Pending</MenuItem>
              <MenuItem value="completed">Completed</MenuItem>
            </Select>
            <Select
              value={filterPriority}
              displayEmpty
              onChange={e => { setFilterPriority(e.target.value); setFilterStatus(''); }}
              sx={{ minWidth: 140 }}
            >
              <MenuItem value="">Filter by Priority</MenuItem>
              <MenuItem value="low">Low</MenuItem>
              <MenuItem value="medium">Medium</MenuItem>
              <MenuItem value="high">High</MenuItem>
            </Select>
            <Button onClick={handleClearFilters}>Clear Filters</Button>
          </Stack>
          <Typography variant="h6" gutterBottom align="center">Tasks</Typography>
          <List>
            {loading ? (
              <ListItem><ListItemText primary="Loading..." /></ListItem>
            ) : tasks.length ? (
              tasks.map((task, idx) => (
                <ListItem key={task.id || idx} divider button onClick={()=>handleTaskClick(task)}>
                  <ListItemText
                    primary={task.title}
                    secondary={`Priority: ${task.priority}`}
                  />
                </ListItem>
              ))
            ) : (
              <ListItem><ListItemText primary="No tasks yet." /></ListItem>
            )}
          </List>
          <Dialog open={!!selectedTask} onClose={()=>setSelectedTask(null)} maxWidth="sm" fullWidth>
            {selectedTask && (
              <TaskDetails
                taskId={selectedTask}
                onClose={()=>setSelectedTask(null)}
                onUpdated={handleTaskUpdated}
                onDeleted={handleTaskDeleted}
              />
            )}
          </Dialog>
          <Dialog open={groupOpen} onClose={()=>setGroupOpen(false)} maxWidth="sm" fullWidth>
            <TaskGroup
              onCreated={()=>{ setGroupOpen(false); fetchTasks(); }}
            />
          </Dialog>
        </Paper>
      </Container>
    </Box>
  );
}

export default App;
