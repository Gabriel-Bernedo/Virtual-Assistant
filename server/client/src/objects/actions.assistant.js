const SS = window.speechSynthesis;
const SR = window.;
export const say = (text) => {
  if(SS.speaking){
    SS.cancel()
  }
  const message = new SpeechSynthesisUtterance()
  message.text = text
  SS.speak(message)
}

const state = {
  hear: false
}

export const hear = () => {
  if(state.hear){
    SR.end()
    return SR.result
  } else {
    
    SR.start()
  }
}