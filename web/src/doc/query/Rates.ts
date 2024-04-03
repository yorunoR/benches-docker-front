const QUERY = /* GraphQL */ `
  query Rates($questionId: ID!) {
    rates(questionId: $questionId) {
      id
      model
      point
      text
      answer {
        id
        text
        finishReason
        usage
        processingTime
      }
    }
    question(id: $questionId) {
      id
      questionNumber
      category
      turns
      bench {
        id
      }
    }
  }
`
export default QUERY