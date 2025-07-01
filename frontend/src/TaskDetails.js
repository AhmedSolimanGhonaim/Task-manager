import React, { useEffect, useState } from 'react';
import { getTask, updateTask, deleteTask } from './api';
import { Box, Typography, Button, TextField, Select, MenuItem, Paper, Stack } from '@mui/material';

export default function TaskDetails({ taskId, onClose, onUpdated, onDeleted }) {
  const [task, setTask] = useState(null);
  const [edit, setEdit] = useState(false);
  const [title, setTitle] = useState('');
  const [priority, setPriority] = useState('medium');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!taskId) return;
    setLoading(true);
    getTask(taskId)
      .then(res => {
        setTask(res.data);
        setTitle(res.data.title);
        setPriority(res.data.priority);
      })
      .finally(() => setLoading(false));
  }, [taskId]);

  const handleUpdate = async () => {
    await updateTask(taskId, { title, priority });
    setEdit(false);
    onUpdated && onUpdated();
  };

  const handleDelete = async () => {
    await deleteTask(taskId);
    onDeleted && onDeleted();
    onClose && onClose();
  };

  if (loading) return <Paper sx={{p:2}}>Loading...</Paper>;
  if (!task) return <Paper sx={{p:2}}>Task not found.</Paper>;

  return (
    <Paper sx={{p:3, mt:2}}>
      <Stack spacing={2}>
        <Typography variant="h6">Task Details</Typography>
        {edit ? (
          <>
            <TextField label="Title" value={title} onChange={e=>setTitle(e.target.value)} fullWidth />
            <Select value={priority} onChange={e=>setPriority(e.target.value)}>
              <MenuItem value="low">Low</MenuItem>
              <MenuItem value="medium">Medium</MenuItem>
              <MenuItem value="high">High</MenuItem>
            </Select>
            <Stack direction="row" spacing={1}>
              <Button variant="contained" onClick={handleUpdate}>Save</Button>
              <Button variant="outlined" onClick={()=>setEdit(false)}>Cancel</Button>
            </Stack>
          </>
        ) : (
          <>
            <Typography>Title: {task.title}</Typography>
            <Typography>Priority: {task.priority}</Typography>
            <Stack direction="row" spacing={1}>
              <Button variant="contained" onClick={()=>setEdit(true)}>Edit</Button>
              <Button variant="outlined" color="error" onClick={handleDelete}>Delete</Button>
              <Button variant="text" onClick={onClose}>Close</Button>
            </Stack>
          </>
        )}
      </Stack>
    </Paper>
  );
}
