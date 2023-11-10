import express, { Request, Response, Application } from 'express'
import dotenv from 'dotenv'
import uploadRouter from './routes/uploadRouter'
import testRouter from './routes/testRouter'
import bodyParser from 'body-parser'
import cors from 'cors'

//For env File 
dotenv.config()

const app: Application = express()
app.use(cors())

const port = process.env.PORT || 5000
app.use(express.urlencoded({ extended: false }))

// for parsing application/json
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: false }))

app.get('/', (req: Request, res: Response) => {
  res.json('Welcome to Express & TypeScript Server')
})

app.use('/api/upload', uploadRouter)
app.use('/api/test', testRouter)

app.listen(port, () => {
  console.log('=========================================')
  console.log(`Server is Fire at http://localhost:${port}`)
  console.log('=========================================')
})

module.exports = app