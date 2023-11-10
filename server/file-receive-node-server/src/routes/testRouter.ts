import express, { Request, Response } from 'express'
import { PythonShell } from 'python-shell';
const router = express.Router()

const options = {
  scriptPath: 'E:\\image_preprocessing',
  args: ['arg1'],
};

router.post('/', (req: Request, res: Response) => {
  if (!req.body) {
    res.status(400).json('Request error')
  } else {
    console.log('---test-->', req.body)
    PythonShell.run('main.py', options,).then(message => {
      console.log('Python script executed successfully!', message)
    })
      .catch(err => console.log('error-->', err))
    res.status(200).json({ res: 'test-->', ...req.body })
  }
})

export default router