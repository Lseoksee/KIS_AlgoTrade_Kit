import { spawn } from "child_process";

// 파이썬 프로세스 실행
const pythonProcess = spawn("python", ["PIC.py"]);

// 파이썬 오류 처리
pythonProcess.stderr.on("data", (data) => {
  console.error(`Python Err__: ${data}`);
});

// 파이썬에서 메시지를 받았을 때 처리
pythonProcess.stdout.on("data", (data) => {
  console.log(`Received from Python : ${data}`);
});

// 메시지 전송
//pythonProcess.stdin.write("Node.js에서 파이썬으로 메시지 전송");
//pythonProcess.stdin.end();

// 파이썬에서 종료되었을 때 처리
pythonProcess.on("close", (code) => {
  console.log(`Python stoped : ${code}`);
});
