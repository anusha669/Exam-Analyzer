export class Answer{
    option_number : number;
    explanation : string;
}

export class QuestionDetails{
    answer: Answer[];
    options: string[];
    question: string;
    questionNumber: number;
}

export class QuestionSet{
    ChapterName : string;
    questionSet: QuestionDetails[];
}

export class ListChapters{
    chapters : string[];
}

// export class ChapterDetails{
//     chapterName: string;
//     completePercent: number;
//     notes : string;
//     resumeAt: number;
// }

// export class UserData{
//     result : { 
//             progress : ChapterDetails[];
//             username : string;
//             }
// }


