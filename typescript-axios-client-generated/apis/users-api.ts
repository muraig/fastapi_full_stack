/* tslint:disable */
/* eslint-disable */
/**
 * FastAPI Vue RabbitMQ PostgreSQL Traefik full set of applications for organizing auto-dialing on Asterisk
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * OpenAPI spec version: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */
import globalAxios, { AxiosPromise, AxiosInstance } from 'axios';
import { Configuration } from '../configuration';
// Some imports not used depending on template conditions
// @ts-ignore
import { BASE_PATH, COLLECTION_FORMATS, RequestArgs, BaseAPI, RequiredError } from '../base';
import { BodyCreateUserOpenApiV1UsersOpenPost } from '../models';
import { BodyUpdateUserMeApiV1UsersMePut } from '../models';
import { HTTPValidationError } from '../models';
import { User } from '../models';
import { UserCreate } from '../models';
import { UserUpdate } from '../models';
/**
 * UsersApi - axios parameter creator
 * @export
 */
export const UsersApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * Create new user.
         * @summary Create User
         * @param {UserCreate} body 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createUserApiV1UsersPost: async (body: UserCreate, options: any = {}): Promise<RequestArgs> => {
            // verify required parameter 'body' is not null or undefined
            if (body === null || body === undefined) {
                throw new RequiredError('body','Required parameter body was null or undefined when calling createUserApiV1UsersPost.');
            }
            const localVarPath = `/api/v1/users/`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, 'https://example.com');
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }
            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options};
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication OAuth2PasswordBearer required
            // oauth required
            if (configuration && configuration.accessToken) {
                const localVarAccessTokenValue = typeof configuration.accessToken === 'function'
                    ? await configuration.accessToken("OAuth2PasswordBearer", [""])
                    : await configuration.accessToken;
                localVarHeaderParameter["Authorization"] = "Bearer " + localVarAccessTokenValue;
            }

            localVarHeaderParameter['Content-Type'] = 'application/json';

            const query = new URLSearchParams(localVarUrlObj.search);
            for (const key in localVarQueryParameter) {
                query.set(key, localVarQueryParameter[key]);
            }
            for (const key in options.query) {
                query.set(key, options.query[key]);
            }
            localVarUrlObj.search = (new URLSearchParams(query)).toString();
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = {...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers};
            const needsSerialization = (typeof body !== "string") || localVarRequestOptions.headers['Content-Type'] === 'application/json';
            localVarRequestOptions.data =  needsSerialization ? JSON.stringify(body !== undefined ? body : {}) : (body || "");

            return {
                url: localVarUrlObj.pathname + localVarUrlObj.search + localVarUrlObj.hash,
                options: localVarRequestOptions,
            };
        },
        /**
         * Create new user without the need to be logged in.
         * @summary Create User Open
         * @param {BodyCreateUserOpenApiV1UsersOpenPost} body 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createUserOpenApiV1UsersOpenPost: async (body: BodyCreateUserOpenApiV1UsersOpenPost, options: any = {}): Promise<RequestArgs> => {
            // verify required parameter 'body' is not null or undefined
            if (body === null || body === undefined) {
                throw new RequiredError('body','Required parameter body was null or undefined when calling createUserOpenApiV1UsersOpenPost.');
            }
            const localVarPath = `/api/v1/users/open`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, 'https://example.com');
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }
            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options};
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            localVarHeaderParameter['Content-Type'] = 'application/json';

            const query = new URLSearchParams(localVarUrlObj.search);
            for (const key in localVarQueryParameter) {
                query.set(key, localVarQueryParameter[key]);
            }
            for (const key in options.query) {
                query.set(key, options.query[key]);
            }
            localVarUrlObj.search = (new URLSearchParams(query)).toString();
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = {...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers};
            const needsSerialization = (typeof body !== "string") || localVarRequestOptions.headers['Content-Type'] === 'application/json';
            localVarRequestOptions.data =  needsSerialization ? JSON.stringify(body !== undefined ? body : {}) : (body || "");

            return {
                url: localVarUrlObj.pathname + localVarUrlObj.search + localVarUrlObj.hash,
                options: localVarRequestOptions,
            };
        },
        /**
         * Get a specific user by id.
         * @summary Read User By Id
         * @param {number} userId 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        readUserByIdApiV1UsersUserIdGet: async (userId: number, options: any = {}): Promise<RequestArgs> => {
            // verify required parameter 'userId' is not null or undefined
            if (userId === null || userId === undefined) {
                throw new RequiredError('userId','Required parameter userId was null or undefined when calling readUserByIdApiV1UsersUserIdGet.');
            }
            const localVarPath = `/api/v1/users/{user_id}`
                .replace(`{${"user_id"}}`, encodeURIComponent(String(userId)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, 'https://example.com');
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }
            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options};
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication OAuth2PasswordBearer required
            // oauth required
            if (configuration && configuration.accessToken) {
                const localVarAccessTokenValue = typeof configuration.accessToken === 'function'
                    ? await configuration.accessToken("OAuth2PasswordBearer", [""])
                    : await configuration.accessToken;
                localVarHeaderParameter["Authorization"] = "Bearer " + localVarAccessTokenValue;
            }

            const query = new URLSearchParams(localVarUrlObj.search);
            for (const key in localVarQueryParameter) {
                query.set(key, localVarQueryParameter[key]);
            }
            for (const key in options.query) {
                query.set(key, options.query[key]);
            }
            localVarUrlObj.search = (new URLSearchParams(query)).toString();
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = {...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers};

            return {
                url: localVarUrlObj.pathname + localVarUrlObj.search + localVarUrlObj.hash,
                options: localVarRequestOptions,
            };
        },
        /**
         * Get current user.
         * @summary Read User Me
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        readUserMeApiV1UsersMeGet: async (options: any = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/users/me`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, 'https://example.com');
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }
            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options};
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication OAuth2PasswordBearer required
            // oauth required
            if (configuration && configuration.accessToken) {
                const localVarAccessTokenValue = typeof configuration.accessToken === 'function'
                    ? await configuration.accessToken("OAuth2PasswordBearer", [""])
                    : await configuration.accessToken;
                localVarHeaderParameter["Authorization"] = "Bearer " + localVarAccessTokenValue;
            }

            const query = new URLSearchParams(localVarUrlObj.search);
            for (const key in localVarQueryParameter) {
                query.set(key, localVarQueryParameter[key]);
            }
            for (const key in options.query) {
                query.set(key, options.query[key]);
            }
            localVarUrlObj.search = (new URLSearchParams(query)).toString();
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = {...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers};

            return {
                url: localVarUrlObj.pathname + localVarUrlObj.search + localVarUrlObj.hash,
                options: localVarRequestOptions,
            };
        },
        /**
         * Retrieve users.
         * @summary Read Users
         * @param {number} [skip] 
         * @param {number} [limit] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        readUsersApiV1UsersGet: async (skip?: number, limit?: number, options: any = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/users/`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, 'https://example.com');
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }
            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options};
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication OAuth2PasswordBearer required
            // oauth required
            if (configuration && configuration.accessToken) {
                const localVarAccessTokenValue = typeof configuration.accessToken === 'function'
                    ? await configuration.accessToken("OAuth2PasswordBearer", [""])
                    : await configuration.accessToken;
                localVarHeaderParameter["Authorization"] = "Bearer " + localVarAccessTokenValue;
            }

            if (skip !== undefined) {
                localVarQueryParameter['skip'] = skip;
            }

            if (limit !== undefined) {
                localVarQueryParameter['limit'] = limit;
            }

            const query = new URLSearchParams(localVarUrlObj.search);
            for (const key in localVarQueryParameter) {
                query.set(key, localVarQueryParameter[key]);
            }
            for (const key in options.query) {
                query.set(key, options.query[key]);
            }
            localVarUrlObj.search = (new URLSearchParams(query)).toString();
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = {...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers};

            return {
                url: localVarUrlObj.pathname + localVarUrlObj.search + localVarUrlObj.hash,
                options: localVarRequestOptions,
            };
        },
        /**
         * Update a user.
         * @summary Update User
         * @param {UserUpdate} body 
         * @param {number} userId 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        updateUserApiV1UsersUserIdPut: async (body: UserUpdate, userId: number, options: any = {}): Promise<RequestArgs> => {
            // verify required parameter 'body' is not null or undefined
            if (body === null || body === undefined) {
                throw new RequiredError('body','Required parameter body was null or undefined when calling updateUserApiV1UsersUserIdPut.');
            }
            // verify required parameter 'userId' is not null or undefined
            if (userId === null || userId === undefined) {
                throw new RequiredError('userId','Required parameter userId was null or undefined when calling updateUserApiV1UsersUserIdPut.');
            }
            const localVarPath = `/api/v1/users/{user_id}`
                .replace(`{${"user_id"}}`, encodeURIComponent(String(userId)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, 'https://example.com');
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }
            const localVarRequestOptions = { method: 'PUT', ...baseOptions, ...options};
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication OAuth2PasswordBearer required
            // oauth required
            if (configuration && configuration.accessToken) {
                const localVarAccessTokenValue = typeof configuration.accessToken === 'function'
                    ? await configuration.accessToken("OAuth2PasswordBearer", [""])
                    : await configuration.accessToken;
                localVarHeaderParameter["Authorization"] = "Bearer " + localVarAccessTokenValue;
            }

            localVarHeaderParameter['Content-Type'] = 'application/json';

            const query = new URLSearchParams(localVarUrlObj.search);
            for (const key in localVarQueryParameter) {
                query.set(key, localVarQueryParameter[key]);
            }
            for (const key in options.query) {
                query.set(key, options.query[key]);
            }
            localVarUrlObj.search = (new URLSearchParams(query)).toString();
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = {...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers};
            const needsSerialization = (typeof body !== "string") || localVarRequestOptions.headers['Content-Type'] === 'application/json';
            localVarRequestOptions.data =  needsSerialization ? JSON.stringify(body !== undefined ? body : {}) : (body || "");

            return {
                url: localVarUrlObj.pathname + localVarUrlObj.search + localVarUrlObj.hash,
                options: localVarRequestOptions,
            };
        },
        /**
         * Update own user.
         * @summary Update User Me
         * @param {BodyUpdateUserMeApiV1UsersMePut} [body] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        updateUserMeApiV1UsersMePut: async (body?: BodyUpdateUserMeApiV1UsersMePut, options: any = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/users/me`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, 'https://example.com');
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }
            const localVarRequestOptions = { method: 'PUT', ...baseOptions, ...options};
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication OAuth2PasswordBearer required
            // oauth required
            if (configuration && configuration.accessToken) {
                const localVarAccessTokenValue = typeof configuration.accessToken === 'function'
                    ? await configuration.accessToken("OAuth2PasswordBearer", [""])
                    : await configuration.accessToken;
                localVarHeaderParameter["Authorization"] = "Bearer " + localVarAccessTokenValue;
            }

            localVarHeaderParameter['Content-Type'] = 'application/json';

            const query = new URLSearchParams(localVarUrlObj.search);
            for (const key in localVarQueryParameter) {
                query.set(key, localVarQueryParameter[key]);
            }
            for (const key in options.query) {
                query.set(key, options.query[key]);
            }
            localVarUrlObj.search = (new URLSearchParams(query)).toString();
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = {...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers};
            const needsSerialization = (typeof body !== "string") || localVarRequestOptions.headers['Content-Type'] === 'application/json';
            localVarRequestOptions.data =  needsSerialization ? JSON.stringify(body !== undefined ? body : {}) : (body || "");

            return {
                url: localVarUrlObj.pathname + localVarUrlObj.search + localVarUrlObj.hash,
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * UsersApi - functional programming interface
 * @export
 */
export const UsersApiFp = function(configuration?: Configuration) {
    return {
        /**
         * Create new user.
         * @summary Create User
         * @param {UserCreate} body 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async createUserApiV1UsersPost(body: UserCreate, options?: any): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<User>> {
            const localVarAxiosArgs = await UsersApiAxiosParamCreator(configuration).createUserApiV1UsersPost(body, options);
            return (axios: AxiosInstance = globalAxios, basePath: string = BASE_PATH) => {
                const axiosRequestArgs = {...localVarAxiosArgs.options, url: basePath + localVarAxiosArgs.url};
                return axios.request(axiosRequestArgs);
            };
        },
        /**
         * Create new user without the need to be logged in.
         * @summary Create User Open
         * @param {BodyCreateUserOpenApiV1UsersOpenPost} body 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async createUserOpenApiV1UsersOpenPost(body: BodyCreateUserOpenApiV1UsersOpenPost, options?: any): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<User>> {
            const localVarAxiosArgs = await UsersApiAxiosParamCreator(configuration).createUserOpenApiV1UsersOpenPost(body, options);
            return (axios: AxiosInstance = globalAxios, basePath: string = BASE_PATH) => {
                const axiosRequestArgs = {...localVarAxiosArgs.options, url: basePath + localVarAxiosArgs.url};
                return axios.request(axiosRequestArgs);
            };
        },
        /**
         * Get a specific user by id.
         * @summary Read User By Id
         * @param {number} userId 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async readUserByIdApiV1UsersUserIdGet(userId: number, options?: any): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<User>> {
            const localVarAxiosArgs = await UsersApiAxiosParamCreator(configuration).readUserByIdApiV1UsersUserIdGet(userId, options);
            return (axios: AxiosInstance = globalAxios, basePath: string = BASE_PATH) => {
                const axiosRequestArgs = {...localVarAxiosArgs.options, url: basePath + localVarAxiosArgs.url};
                return axios.request(axiosRequestArgs);
            };
        },
        /**
         * Get current user.
         * @summary Read User Me
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async readUserMeApiV1UsersMeGet(options?: any): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<User>> {
            const localVarAxiosArgs = await UsersApiAxiosParamCreator(configuration).readUserMeApiV1UsersMeGet(options);
            return (axios: AxiosInstance = globalAxios, basePath: string = BASE_PATH) => {
                const axiosRequestArgs = {...localVarAxiosArgs.options, url: basePath + localVarAxiosArgs.url};
                return axios.request(axiosRequestArgs);
            };
        },
        /**
         * Retrieve users.
         * @summary Read Users
         * @param {number} [skip] 
         * @param {number} [limit] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async readUsersApiV1UsersGet(skip?: number, limit?: number, options?: any): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Array<User>>> {
            const localVarAxiosArgs = await UsersApiAxiosParamCreator(configuration).readUsersApiV1UsersGet(skip, limit, options);
            return (axios: AxiosInstance = globalAxios, basePath: string = BASE_PATH) => {
                const axiosRequestArgs = {...localVarAxiosArgs.options, url: basePath + localVarAxiosArgs.url};
                return axios.request(axiosRequestArgs);
            };
        },
        /**
         * Update a user.
         * @summary Update User
         * @param {UserUpdate} body 
         * @param {number} userId 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async updateUserApiV1UsersUserIdPut(body: UserUpdate, userId: number, options?: any): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<User>> {
            const localVarAxiosArgs = await UsersApiAxiosParamCreator(configuration).updateUserApiV1UsersUserIdPut(body, userId, options);
            return (axios: AxiosInstance = globalAxios, basePath: string = BASE_PATH) => {
                const axiosRequestArgs = {...localVarAxiosArgs.options, url: basePath + localVarAxiosArgs.url};
                return axios.request(axiosRequestArgs);
            };
        },
        /**
         * Update own user.
         * @summary Update User Me
         * @param {BodyUpdateUserMeApiV1UsersMePut} [body] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async updateUserMeApiV1UsersMePut(body?: BodyUpdateUserMeApiV1UsersMePut, options?: any): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<User>> {
            const localVarAxiosArgs = await UsersApiAxiosParamCreator(configuration).updateUserMeApiV1UsersMePut(body, options);
            return (axios: AxiosInstance = globalAxios, basePath: string = BASE_PATH) => {
                const axiosRequestArgs = {...localVarAxiosArgs.options, url: basePath + localVarAxiosArgs.url};
                return axios.request(axiosRequestArgs);
            };
        },
    }
};

/**
 * UsersApi - factory interface
 * @export
 */
export const UsersApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    return {
        /**
         * Create new user.
         * @summary Create User
         * @param {UserCreate} body 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createUserApiV1UsersPost(body: UserCreate, options?: any): AxiosPromise<User> {
            return UsersApiFp(configuration).createUserApiV1UsersPost(body, options).then((request) => request(axios, basePath));
        },
        /**
         * Create new user without the need to be logged in.
         * @summary Create User Open
         * @param {BodyCreateUserOpenApiV1UsersOpenPost} body 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createUserOpenApiV1UsersOpenPost(body: BodyCreateUserOpenApiV1UsersOpenPost, options?: any): AxiosPromise<User> {
            return UsersApiFp(configuration).createUserOpenApiV1UsersOpenPost(body, options).then((request) => request(axios, basePath));
        },
        /**
         * Get a specific user by id.
         * @summary Read User By Id
         * @param {number} userId 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        readUserByIdApiV1UsersUserIdGet(userId: number, options?: any): AxiosPromise<User> {
            return UsersApiFp(configuration).readUserByIdApiV1UsersUserIdGet(userId, options).then((request) => request(axios, basePath));
        },
        /**
         * Get current user.
         * @summary Read User Me
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        readUserMeApiV1UsersMeGet(options?: any): AxiosPromise<User> {
            return UsersApiFp(configuration).readUserMeApiV1UsersMeGet(options).then((request) => request(axios, basePath));
        },
        /**
         * Retrieve users.
         * @summary Read Users
         * @param {number} [skip] 
         * @param {number} [limit] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        readUsersApiV1UsersGet(skip?: number, limit?: number, options?: any): AxiosPromise<Array<User>> {
            return UsersApiFp(configuration).readUsersApiV1UsersGet(skip, limit, options).then((request) => request(axios, basePath));
        },
        /**
         * Update a user.
         * @summary Update User
         * @param {UserUpdate} body 
         * @param {number} userId 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        updateUserApiV1UsersUserIdPut(body: UserUpdate, userId: number, options?: any): AxiosPromise<User> {
            return UsersApiFp(configuration).updateUserApiV1UsersUserIdPut(body, userId, options).then((request) => request(axios, basePath));
        },
        /**
         * Update own user.
         * @summary Update User Me
         * @param {BodyUpdateUserMeApiV1UsersMePut} [body] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        updateUserMeApiV1UsersMePut(body?: BodyUpdateUserMeApiV1UsersMePut, options?: any): AxiosPromise<User> {
            return UsersApiFp(configuration).updateUserMeApiV1UsersMePut(body, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * UsersApi - object-oriented interface
 * @export
 * @class UsersApi
 * @extends {BaseAPI}
 */
export class UsersApi extends BaseAPI {
    /**
     * Create new user.
     * @summary Create User
     * @param {UserCreate} body 
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof UsersApi
     */
    public createUserApiV1UsersPost(body: UserCreate, options?: any) {
        return UsersApiFp(this.configuration).createUserApiV1UsersPost(body, options).then((request) => request(this.axios, this.basePath));
    }
    /**
     * Create new user without the need to be logged in.
     * @summary Create User Open
     * @param {BodyCreateUserOpenApiV1UsersOpenPost} body 
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof UsersApi
     */
    public createUserOpenApiV1UsersOpenPost(body: BodyCreateUserOpenApiV1UsersOpenPost, options?: any) {
        return UsersApiFp(this.configuration).createUserOpenApiV1UsersOpenPost(body, options).then((request) => request(this.axios, this.basePath));
    }
    /**
     * Get a specific user by id.
     * @summary Read User By Id
     * @param {number} userId 
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof UsersApi
     */
    public readUserByIdApiV1UsersUserIdGet(userId: number, options?: any) {
        return UsersApiFp(this.configuration).readUserByIdApiV1UsersUserIdGet(userId, options).then((request) => request(this.axios, this.basePath));
    }
    /**
     * Get current user.
     * @summary Read User Me
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof UsersApi
     */
    public readUserMeApiV1UsersMeGet(options?: any) {
        return UsersApiFp(this.configuration).readUserMeApiV1UsersMeGet(options).then((request) => request(this.axios, this.basePath));
    }
    /**
     * Retrieve users.
     * @summary Read Users
     * @param {number} [skip] 
     * @param {number} [limit] 
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof UsersApi
     */
    public readUsersApiV1UsersGet(skip?: number, limit?: number, options?: any) {
        return UsersApiFp(this.configuration).readUsersApiV1UsersGet(skip, limit, options).then((request) => request(this.axios, this.basePath));
    }
    /**
     * Update a user.
     * @summary Update User
     * @param {UserUpdate} body 
     * @param {number} userId 
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof UsersApi
     */
    public updateUserApiV1UsersUserIdPut(body: UserUpdate, userId: number, options?: any) {
        return UsersApiFp(this.configuration).updateUserApiV1UsersUserIdPut(body, userId, options).then((request) => request(this.axios, this.basePath));
    }
    /**
     * Update own user.
     * @summary Update User Me
     * @param {BodyUpdateUserMeApiV1UsersMePut} [body] 
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof UsersApi
     */
    public updateUserMeApiV1UsersMePut(body?: BodyUpdateUserMeApiV1UsersMePut, options?: any) {
        return UsersApiFp(this.configuration).updateUserMeApiV1UsersMePut(body, options).then((request) => request(this.axios, this.basePath));
    }
}