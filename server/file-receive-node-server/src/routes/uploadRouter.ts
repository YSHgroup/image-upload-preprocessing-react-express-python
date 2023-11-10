import { Request, Response, Router } from 'express'
import { PythonShell } from 'python-shell'
import { upload } from '@/midlewares';


const router = Router()

// POST /upload
router.post('/', upload.array('files'), (req: Request, res: Response) => {

  if (!req.files || !req.files.length) return res.status(400).send({ res: null, ...req.body, err: "fiald to upload file" })
  console.log('--start file preprocessing--')
  const files = (req.files as Express.Multer.File[]).map((file: Express.Multer.File) => file.originalname)
  const options = {
    scriptPath: 'E:\\My work\\image_preprocessing',
    args: files,
  }
  PythonShell.run('main.py', options)
    .then(message => {
      console.log('Python script executed successfully!  \n', message, '\n--------------------');
    })
    .catch(err => console.log('error-->', err))

  res.status(200).json({ res: 'File Uploaded', ...req.body })
})

export default router