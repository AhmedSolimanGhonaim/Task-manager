import React, { useState } from 'react';
import { createManyTasks } from './api';
import { Box, Typography, Button, TextField, Paper, Stack } from '@mui/material';

export default function TaskGroup({ onCreated }) {
  const [tasks, setTasks] = useState([{ title: '', priority: 'medium' }]);
  const [loading, setLoading] = useState(false);

  const handleChange = (idx, field, value) => {
    setTasks(tasks => tasks.map((t, i) => i === idx ? { ...t, [field]: value } : t));
  };

  const handleAddRow = () => {
    setTasks([...tasks, { title: '', priority: 'medium' }]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    await createManyTasks(tasks);
    setTasks([{ title: '', priority: 'medium' }]);
    setLoading(false);
    onCreated && onCreated();
  };

  return (
    <Paper sx={{p:3, mt:2}}>
      <Typography variant="h6">Create Multiple Tasks</Typography>
      <Box component="form" onSubmit={handleSubmit}>
        <Stack spacing={2}>
          {tasks.map((task, idx) => (
            <Stack direction="row" spacing={2} key={idx}>
              <TextField label="Title" value={task.title} onChange={e=>handleChange(idx,'title',e.target.value)} required />
              <TextField label="Priority" value={task.priority} onChange={e=>handleChange(idx,'priority',e.target.value)} required />
            </Stack>
          ))}
          <Button onClick={handleAddRow}>Add Another</Button>
          <Button type="submit" variant="contained" disabled={loading}>Create All</Button>
        </Stack>
      </Box>
    </Paper>
  );
}
