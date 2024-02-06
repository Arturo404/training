import * as repl from 'repl';

const options = { useColors: true, prompt: '> ' };
const repl_instance = repl.start(options);
repl_instance.defineCommand('sayhello', {
    help: 'Say hello',
    action(name) {
      this.clearBufferedCommand();
      console.log(`Hello, ${name}!`);
      this.displayPrompt();
    },
});